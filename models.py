__author__ = 'sean.braley'


class Book(object):
    '''Simple ebook object, will be replaced later by calbre'''

    def __init__(self, title, author, genre, keyword, text):
        self.title = title
        self.author = author
        self.genre = genre
        self.keyword = keyword
        self.text = text

    def __str__(self):
        return u'%s, by %s' % (self.title, self.author)

    def estimate_writing_style_fuzzy(self):
        '''return a fuzzy value for style of writing, range [pulp .. monologue]'''
        # Estimate based on author
        author = .5

        # Estimate based on stated genre
        genre = .5

        # Estimate based on loosely parsing the text