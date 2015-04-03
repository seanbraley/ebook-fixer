# -*- coding: utf-8 -*-
__author__ = 'sean.braley'

import re

from models import Book

import nltk
import codecs

# Load up PUNKT sentence detector (this works well)
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

print("Performing analysis and formatting on several books, this might take some time.")


# Wiz Oz book:
print("\nWizard of Oz: ")

with open('wiz_oz.txt', 'rb') as file:
    fileText = file.read()

fileText = fileText.replace("\n", "")
fileText = fileText.split("\r")

while '' in fileText:
    fileText.remove('')

para_lengths = []
sentences_complete = []
num_paragraphs = 0
for paragraph in fileText:
    sentences = sent_detector.tokenize(paragraph.strip())
    para_lengths.append(len(sentences))
    num_paragraphs += 1

    sentences_complete.extend(sentences)

theWizard = Book('The Wizard of Oz', ':. Frank Baum', 'adventure', sentences_complete)
theWizard.estimate_pulpiness_fuzzy()

theWizard.format()

print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    num_paragraphs,
    len(theWizard.paragraphs)
))


# Keneth Robeson book:
print("\nDoc Savage: ")

with open('Doc Savage - 001 - The Man of Bronze(1933)(Dent, Lester).txt', 'rb') as file:
    fileText = file.read()

fileText = fileText.replace("\n", "")
fileText = fileText.split("\r")

while '' in fileText:
    fileText.remove('')

para_lengths = []
num_paragraphs = 0
sentences_complete = []
for paragraph in fileText:
    sentences = sent_detector.tokenize(paragraph.strip())
    para_lengths.append(len(sentences))
    num_paragraphs += 1
    sentences_complete.extend(sentences)

docSavageFirst = Book('Doc Savage - 001 The Man of Bronze', 'Keneth Robeson', 'mystery;adventure', sentences_complete)
docSavageFirst.estimate_pulpiness_fuzzy()

docSavageFirst.format()

with codecs.open('outputfile.txt', 'w', 'utf-8') as output:
    output.write(docSavageFirst.corrected_text)


print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    num_paragraphs,
    len(docSavageFirst.paragraphs)
))
'''

print("Average Paragraph Length: {0:.2f} sentences; Max: {1:.2f}; Min {2:.2f}".format(average(para_lengths),
                                                                                      max(para_lengths),
                                                                                      min(para_lengths)))

print("Number of 1-sentence paragraphs: {0} out of {1} paragraphs".format(para_lengths.count(1),
                                                                          len(para_lengths)))
'''


# Keneth Robeson book:
print("\nDoc Savage 13: ")

with open('Doc Savage - 013 - Land of Always-Night(1935)(Dent, Lester).txt', 'rb') as file:
    fileText = file.read()

fileText = fileText.replace("\n", "")
fileText = fileText.split("\r")

while '' in fileText:
    fileText.remove('')

para_lengths = []
sentences_complete = []
num_paragraphs = 0
for paragraph in fileText:
    sentences = sent_detector.tokenize(paragraph.strip())
    para_lengths.append(len(sentences))
    num_paragraphs += 1

    sentences_complete.extend(sentences)

docSavageSecond = Book('Doc Savage - 013 Land of Always-Night', 'Keneth Robeson', 'mystery;adventure', sentences_complete)
docSavageSecond.estimate_pulpiness_fuzzy()

docSavageSecond.format()

print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    num_paragraphs,
    len(docSavageSecond.paragraphs)
))

# Enable for stats
'''
print("Average Paragraph Length: {0:.2f} sentences; Max: {1:.2f}; Min {2:.2f}".format(average(para_lengths),
                                                                                      max(para_lengths),
                                                                                      min(para_lengths)))

print("Number of 1-sentence paragraphs: {0} out of {1} paragraphs".format(para_lengths.count(1),
                                                                          len(para_lengths)))
'''


print("\nEmma: ")


theAustenBook = Book('Emma', 'Jane Austen', 'Novel of manners', nltk.corpus.gutenberg.sents('austen-emma.txt'))
theAustenBook.estimate_pulpiness_fuzzy()

theAustenBook.format()

print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    len(nltk.corpus.gutenberg.paras('austen-emma.txt')),
    len(theAustenBook.paragraphs)
))

# Enable for stats
'''
print("Average Paragraph Length: {0:.2f} sentences; Max: {1:.2f}; Min {2:.2f}".format(average(para_lengths),
                                                                                      max(para_lengths),
                                                                                      min(para_lengths)))

print("Number of 1-sentence paragraphs: {0} out of {1} paragraphs".format(para_lengths.count(1),
                                                                          len(para_lengths)))
'''

print("\nMoby Dick: ")

theMobyDickBook = Book('Moby Dick', 'Melville', 'Adventure', nltk.corpus.gutenberg.sents('melville-moby_dick.txt'))
theMobyDickBook.estimate_pulpiness_fuzzy()

theMobyDickBook.format()

print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    len(nltk.corpus.gutenberg.paras('melville-moby_dick.txt')),
    len(theMobyDickBook.paragraphs)
))

with codecs.open('outputfile2.txt', 'w', 'utf-8') as output:
    output.write(theMobyDickBook.corrected_text)

# Enable for stats
'''
print("Average Paragraph Length: {0:.2f} sentences; Max: {1:.2f}; Min {2:.2f}".format(average(para_lengths),
                                                                                      max(para_lengths),
                                                                                      min(para_lengths)))

print("Number of 1-sentence paragraphs: {0} out of {1} paragraphs".format(para_lengths.count(1),
                                                                          len(para_lengths)))
'''

# chesterton-brown
print("\nChesterton: ")

theChestertonBook = Book('The Wisdom of Father Brown', 'G. K. Chesterton', 'Mystery', nltk.corpus.gutenberg.sents('chesterton-brown.txt'))
theChestertonBook.estimate_pulpiness_fuzzy()

theChestertonBook.format()

print("Paragraph Breaks\nOriginal: {0}, Formated: {1}".format(
    len(nltk.corpus.gutenberg.paras('chesterton-brown.txt')),
    len(theChestertonBook.paragraphs)
))

# Enable for stats
'''
print("Average Paragraph Length: {0:.2f} sentences; Max: {1:.2f}; Min {2:.2f}".format(average(para_lengths),
                                                                                      max(para_lengths),
                                                                                      min(para_lengths)))

print("Number of 1-sentence paragraphs: {0} out of {1} paragraphs".format(para_lengths.count(1),
                                                                          len(para_lengths)))
'''
