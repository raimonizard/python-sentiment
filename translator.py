from textblob import TextBlob
import csv
from langdetect import detect

# open the csv file called text.csv
# read the file
# skip the header
# generate the script

def iterate_file():
    with open('text.csv', 'r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        next(csv_reader)

        for row in csv.reader(csv_file, delimiter=';'):
            if row[0] != 'id':
                print(row[1])
                print(translation(row[1]))

def translation(text):
    blob = TextBlob(text)
    language = detect(text)

    if language == 'ca':
        return str(text)
    else:
        translation = blob.translate(from_lang=language, to='ca')
        return str(translation)

iterate_file()