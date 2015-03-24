__author__ = 'sean.braley'

from knowledge_base import genres_pulp, authors_pulp


def t_norm(x, y):
    return min(1, x+y)


class Book(object):
    '''Simple ebook object, will be replaced later by calbre'''
    author_weight = .3
    genre_weight = .3
    text_weight = .8

    def __init__(self, title, author, genre, text, pulp_value=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.text = text

        # A value in the range [0..1]
        self.pulp_value = pulp_value

    def __str__(self):
        return u'%s, by %s' % (self.title, self.author)

    def estimate_pulpiness_fuzzy(self):
        '''Sets the value for pulpiness based on the auther, genre and text content'''
        author_value = 1 if self.author in authors_pulp['high'] else 0

        genre_value = 1 if self.genre in genres_pulp['high'] else 0

        # Analyze text
        shortwords = 0
        for word in self.text.split(" "):
            if len(word) > 5:
                shortwords += 1

        # Will range from 0..1
        shortwords_percentage = float(shortwords)/float(len(self.text.split(" ")))
        print shortwords_percentage

        # Calculation:
        # (author_weight ^ author_value) ^ (genre_weight ^ genre_value) ^ (shortword_percentage ^ text_weight)
        self.pulp_value = t_norm(
            t_norm(
                t_norm(self.author_weight, author_value),
                t_norm(self.genre_weight, genre_value)
            ),
            t_norm(self.text_weight, shortwords_percentage)
        )