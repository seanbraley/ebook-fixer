__author__ = 'sean.braley'

import re

from knowledge_base import genres_pulp, authors_pulp


class Book(object):
    '''Simple ebook object, will be replaced later by calbre'''

    def __init__(self, title, author, genre, text, pulp_value=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.text = text
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
        return x*y

    def s_norm(self, x, y, *args):
        if args:
            return self.s_norm(
                self.s_norm(x, y),
                args[0],
                *args[1:]
            )
        return max(x, y)

    def format(self):
        if self.pulp_value is None:
            self.estimate_pulpiness_fuzzy()

        # Textual Indicators
        speaking = r'\"(.+?)\"'
        sentence = r'(.+?)(\.\s|\!\s|\?\s|\.\"\s|\?\"\s)'
        sentences = re.findall(sentence, self.text)
        length = 1
        for sentence in sentences:
            is_speaking = 1.0 if re.match(speaking, sentence[0]) else 0
            charchange = .7 if sentence[0].startswith(('A', 'The')) else 0
            timechange = .7 if sentence[0].startswith(('Once', 'Later', 'This afternoon', 'Tonight', "Tomorrow",
                                                       'Soon', 'Afterwards')) else 0
            placechange = .7 if sentence[0].startswith(('Across', 'Over', 'Under', 'Behind', 'Around', 'Near')) else 0

            do_break = self.s_norm(is_speaking, charchange, timechange, placechange, length/10.0)

            conversion_dict = {
                "VERY HIGH": 0.9,
                "HIGH": 0.7,
                "MEDIUM": 0.5,
                "LOW": 0.3,
                "VERY LOW": 0.1,
            }

            new_break = self.t_norm(do_break, conversion_dict[self.pulp_value])

            # print "Values: {0}, {1}, {2}".format(new_break, do_break, conversion_dict[self.pulp_value])
            self.corrected_text += sentence[0]
            if do_break >= 0.5:
                self.corrected_text += "\n"
                length = 1
            else:
                self.corrected_text += " "
                length += 1

            print(self.corrected_text[2000:3000])

    def estimate_pulpiness_fuzzy(self):
        '''Sets the value for pulpiness based on the auther, genre and text content'''
        author_pulp = "HIGH" if self.author in authors_pulp['high'] else "LOW"

        genre_pulp = "HIGH" if self.genre in genres_pulp['high'] else "LOW"

        # Analyze text
        shortwords = 0
        for word in self.text.split(" "):
            if len(word) > 5:
                shortwords += 1
        # Will range from 0..1
        shortwords_percentage = float(shortwords)/float(len(self.text.split(" ")))
        print shortwords_percentage

        if shortwords_percentage >= .30:
            text_pulp = "VERY HIGH"
        elif .30 > shortwords_percentage >= .25:
            text_pulp = "HIGH"
        elif .20 > shortwords_percentage >= .15:
            text_pulp = "MEDIUM"
        elif .15 > shortwords_percentage >= .20:
            text_pulp = "LOW"
        elif .10 > shortwords_percentage >= .15:
            text_pulp = "VERY LOW"
        else:
            text_pulp = "VERY LOW"

        print "Text pulp: " + text_pulp
        print "Author pulp: " + author_pulp
        print "Genre pulp: " + genre_pulp

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

        else:
            print "Missed case! author_pulp: {0}, genre_pulp: {1}, text_pulp: {2}".format(author_pulp, genre_pulp,
                                                                                          text_pulp)

        print "Discovered pulp value: {0}".format(self.pulp_value)