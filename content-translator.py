# Given a file called text.csv with two columns
# id, text
# Generate a script which generates a new file called text_translated.csv
# The new file should have the same structure as the original file plus a new column with the translation of the text to catalan
# The translation should be done using the TextBlob library
# The translation should be done using the translate function
# The translation should be done using the from_lang parameter
# The translation should be done using the to parameter
# The translation should be done using the detect_language function
# The translation should be done using the detect function
# The translation should be done using the detect_language function
# The translation should be done using the detect function
# The translation should be done using the detect_language function

import csv
from textblob import TextBlob

# Read the csv file
with open('text.csv', 'r', encoding='utf8') as csv_file:
    
        csv_reader = csv.reader(csv_file, delimiter=';')
    
        # Skip the header
        next(csv_reader)
    
        # Open a new csv file
        with open('text_translated.csv', 'w', newline='', encoding='utf8') as csv_file:
    
            csv_writer = csv.writer(csv_file, delimiter=';')
    
            # Write the header
            csv_writer.writerow(['id', 'text', 'text_translated'])
    
            # For each row
            for row in csv_reader:
    
                # Get the text
                text = row[1]
                print(text)
    
                # Create a TextBlob object
                text_blob = TextBlob(text)
    
                # Get the language
                language = text_blob.detect_language()
    
                # If the language is not english
                if language != 'en':
    
                    # Translate the text to english
                    text = text_blob.translate(from_lang=language, to='en')
    
                # Create a TextBlob object
                text_blob = TextBlob(text)
    
                # Get the translation
                translation = text_blob.translate(to='ca')
    
                # Write the row
                csv_writer.writerow([row[0], row[1], translation])
    
        # close the file
        csv_file.close()

        