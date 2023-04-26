# Given a file called text.csv with two columns
# id, text
# Generate a script which generates a new file called text_translated.csv
# The new file should have the same structure as the original file plus a new column with the translation of the text to catalan
# The translation should be done using the Google Translate API

import csv
from deep_translator import GoogleTranslator


def iterate_file():
    with open('text.csv', 'r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        next(csv_reader)

        for row in csv.reader(csv_file, delimiter=';'):
            if row[0] != 'id':
                print(row[1])
                print(translation(row[1]))

def translation(text): # Use Google API to translate text
    translator = GoogleTranslator(source='auto', target='ca')
    res = translator.translate(text)
    return str(res)


iterate_file()






