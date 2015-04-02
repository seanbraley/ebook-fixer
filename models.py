__author__ = 'sean.braley'

import re
import math
import nltk

from knowledge_base import genres_pulp, authors_pulp, transition_words, exclusion_words

from utils import sylco


def average(l):
    return reduce(lambda x, y: x + y, l) / float(len(l))


# http://stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


class Book(object):
    '''Simple ebook object, will be replaced later by calbre'''

    def __init__(self, title, author, genre, sentences, pulp_value=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.sentences = sentences
        self.corrected_text = ""
        self.paragraphs = []

        # A value in the range [0..1]
        self.pulp_value = pulp_value

    def __str__(self):
        return u'%s, by %s' % (self.title, self.author)

    def t_norm(self, x, y, *args):
        if args:
            return self.t_norm(
                self.t_norm(x, y),
                args[0],
                *args[1:]
            )
        # Goguen
        return min(x, y)

        # Zukasiewiez
        # return max(0, x+y-1)

        # Nilpotent
        # return min(x, y) if (x + y > 1) else 0

    def s_norm(self, x, y, *args):
        if args:
            return self.s_norm(
                self.s_norm(x, y),
                args[0],
                *args[1:]
            )
        # Goguen
        # return max(x, y)

        # Zukasiewiez
        # return min(1, x+y)

        # Nilpotent
        return max(x, y) if (x + y > 1) else 1

    def format(self):
        if self.pulp_value is None:
            self.estimate_pulpiness_fuzzy()

        # Textual Indicators
        speaking = r'\"(.+?)\"'
        # sentence = r'(.+?)(\.\s|\!\s|\?\s|\.\"\s|\?\"\s)'
        # sentences = re.findall(sentence, self.text)

        length = 1

        """
        Some thoughtspace here...

        In the below code what is really happening is only one of these will ever match bcs its really a giant case statement

        NEED TO FUZZY TRACK CHANGES IN PERSPECTIVE. KEYWORDS ARE NOT ENOUGH


        """
        subject = {}
        for sentence in self.sentences:
            # Speaking (ALWAYS BREAK)
            is_speaking = 1.0 if re.match(speaking, sentence[0]) else 0

            # Keyword, sometimes break
            if sentence[0].startswith(('A', 'The')):
                keyword = .7
            elif sentence[0].startswith(('Once', 'Later', 'This afternoon', 'Tonight', "Tomorrow", 'Soon', 'Afterwards')):
                keyword = .7
            elif sentence[0].startswith(('Across', 'Over', 'Under', 'Behind', 'Around', 'Near')):
                keyword = .7
            elif sentence[0].startswith(transition_words['adverbs']):
                keyword = 0.7
            elif sentence[0].startswith(transition_words['phrases']):
                keyword = 0.5
            elif sentence[0].startswith(transition_words['implied']):
                keyword = 0.3
            elif sentence[0].startswith(transition_words['custom']):
                keyword = 0.7
            else:
                keyword = 0.0

            # Context check (Add this)
            # subject['subject'] = score
            if subject[max(subject)] < 5:
                context = .7
            else:
                context = .3

            do_break = self.s_norm(is_speaking, keyword, context, sigmoid(length/5.0))

            conversion_dict = {
                "VERY HIGH": 0.9,
                "HIGH": 0.7,
                "MEDIUM": 0.5,
                "LOW": 0.3,
                "VERY LOW": 0.1,
            }

            new_break = self.t_norm(do_break, conversion_dict[self.pulp_value])

            # print "Values: {0}, {1}, {2}".format(new_break, do_break, conversion_dict[self.pulp_value])
            # print new_break
            if new_break >= 0.5:
                self.corrected_text += "\n\n"
                subject = {}
                length = 1
            else:
                length += 1

            # Do line break before you add the sentence
            self.corrected_text += sentence[0] + sentence[1]
            self.corrected_text += " "

    def estimate_pulpiness_fuzzy(self):
        '''Sets the value for pulpiness based on the auther, genre and text content'''
        author_pulp = "HIGH" if self.author in authors_pulp['high'] else "LOW"

        genre_pulp = "HIGH" if self.genre in genres_pulp['high'] else "LOW"

        # Analyze text

        # Average sentence length and word length
        shortwords = 0
        exception_words = 0
        word_lengths = []
        sentence_lengths = []
        sylco_lengths = []
        for sentence in self.sentences:
            words = nltk.word_tokenize(sentence) if type(sentence) is not list else sentence

            sentence_length = len(words)
            for word in words:
                word_length = len(word)
                if word_length < 5 and word not in exclusion_words:
                    shortwords += 1
                # These are short words that should not contribute to count
                elif word in exclusion_words:
                    exception_words += 1
                word_lengths.append(word_length)
                sylco_lengths.append(sylco(word))
            sentence_lengths.append(sentence_length)

        # Calculate averages

        # Shortwords Percentage
        # print("shortwords: {0}, len(word_lengths): {1}, exception_words: {2}".format(shortwords, len(word_lengths), exception_words))

        shortwords_percentage = float(shortwords)/float(len(word_lengths)-exception_words)

        # Average word length
        average_word_length = average(word_lengths)

        # Average sentence length
        average_sentence_length = average(sentence_lengths)

        average_sylco_length = average(sylco_lengths)

        # Flesh Reading Ease 100 pt scale
        flesh_score = 206.835 - (1.015 * average_sentence_length) - (84.6 * average_sylco_length)

        # Flesh Kincaid gives grade lvl
        flesh_kincaid_score = (.39 * average_sentence_length) + (11.8 * average_sylco_length) - 15.59

        # SMOG score gives grade lvl
        number_polysyllables = 0
        for x in sylco_lengths:
            if x > 2:
                number_polysyllables += 1

        smog_score = 1.0430 * math.sqrt(number_polysyllables * (30/float(len(sentence_lengths)))) + 3.1291

        #print("Stats: \nShortwords Percentage: {0:.2f}%; Average Word Length: {1:.2f} letters; "
        #      "Average Sentence Length: {2:.2f} words; average syllable length: {3:.2f}"
        #      .format(shortwords_percentage*100, average_word_length,
        #              average_sentence_length, average_sylco_length))

        #print("Reading tests: \nFlesh Reading Ease: {0}, Flesh Kincaid: {1}, SMOG: {2}".format(
        #    flesh_score,
        #    flesh_kincaid_score,
        #    smog_score
        #))

        text_pulp = self.s_norm(
            flesh_score/100.0,
            # Not working well
            # sigmoid(flesh_kincaid_score/10.0),
            # 1.8 - (smog_score/10.0)
            sigmoid(smog_score/12.0)
        )

        if text_pulp > .85:
            text_pulp = "VERY HIGH"
        elif .8 < text_pulp <= .85:
            text_pulp = "HIGH"
        elif .75 < text_pulp <= .8:
            text_pulp = "MEDIUM"
        elif .7 < text_pulp <= .75:
            text_pulp = "LOW"
        elif text_pulp <= .7:
            text_pulp = "VERY LOW"

        # print("Text pulp: {0}, Author pulp: {1}, Genre pulp: {2}".format(text_pulp, author_pulp, genre_pulp))


        # Fuzzy if-then rules:
        if author_pulp is "LOW" and genre_pulp is "LOW" and text_pulp in ("LOW", "VERY LOW"):
            self.pulp_value = "VERY LOW"

        elif author_pulp is "LOW" and genre_pulp is "LOW" and text_pulp is "MEDIUM":
            self.pulp_value = "MEDIUM"

        elif author_pulp is "HIGH" and genre_pulp is "LOW" and text_pulp in ("LOW", "VERY LOW"):
            self.pulp_value = "LOW"

        elif author_pulp is "LOW" and genre_pulp is "HIGH" and text_pulp in ("LOW", "VERY LOW"):
            self.pulp_value = "LOW"

        elif author_pulp is "HIGH" and genre_pulp is "LOW" and text_pulp in ("MEDIUM", "LOW"):
            self.pulp_value = "MEDIUM"

        elif author_pulp is "LOW" and genre_pulp is "HIGH" and text_pulp in ("MEDIUM", "LOW"):
            self.pulp_value = "MEDIUM"

        elif author_pulp is "HIGH" and genre_pulp is "LOW" and text_pulp in ("HIGH", "VERY HIGH"):
            self.pulp_value = "HIGH"

        elif author_pulp is "LOW" and genre_pulp is "HIGH" and text_pulp in ("HIGH", "VERY HIGH"):
            self.pulp_value = "HIGH"

        elif author_pulp is "HIGH" and genre_pulp is "HIGH" and text_pulp is "VERY LOW":
            self.pulp_value = "VERY LOW"

        elif author_pulp is "HIGH" and genre_pulp is "HIGH" and text_pulp is "LOW":
            self.pulp_value = "LOW"

        elif author_pulp is "HIGH" and genre_pulp is "HIGH" and text_pulp in ("MEDIUM", "HIGH"):
            self.pulp_value = "HIGH"

        elif author_pulp is "HIGH" and genre_pulp is "HIGH" and text_pulp is "VERY HIGH":
            self.pulp_value = "VERY HIGH"

        elif author_pulp is "LOW" and genre_pulp is "LOW" and text_pulp in ("HIGH",  "VERY HIGH"):
            self.pulp_value = "HIGH"

        else:
            print "Missed case! author_pulp: {0}, genre_pulp: {1}, text_pulp: {2}".format(author_pulp, genre_pulp,
                                                                                          text_pulp)

        print("Discovered pulp value: {0}".format(self.pulp_value))