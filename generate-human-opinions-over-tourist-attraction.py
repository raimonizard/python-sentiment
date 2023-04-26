# Given a csv file called sentiment-tourist-atraction_v1.csv
# With four columns: id, global_score, agregate_count, tourist-atracttion, opinion
# Create an script which generates a random human opinion for each tourist-atraction
# The human opinion should be a text field something like "I like it" or "I don't like it"
# The human opinion should be generated randomly based on the global_score

import csv
import random

# Read the csv file
with open('sentiment-tourist-atraction_v1.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    # Skip the header
    next(csv_reader)
    # For each row
    for row in csv_reader:
        # Get the global_score
        global_score = float(row[1])
        # Generate a random number between 0 and 1
        random_number = random.random()
        # If the random number is less than the global_score
        if random_number < global_score:
            # Generate a random opinion
            opinion = random.choice(['I hate it', 'I don\'t like it'])
        # If the random number is greater than the global_score
        else:
            # Generate a random opinion
            opinion = random.choice(['I like it', 'I love it'])
        # Print the tourist-atraction and the opinion
        print(row[3], opinion)

# With the results, generate a new output csv file including the human opinion
# The output csv file should have the same structure as the input csv file
# The output csv file should be called sentiment-tourist-atraction_v2.csv

# Read the csv file
with open('sentiment-tourist-atraction_v1.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    # Open a new csv file
    with open('sentiment-tourist-atraction_v2.csv', 'w', newline='', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        # Write the header
        csv_writer.writerow(['id', 'global_score', 'agregate_count', 'tourist-atraction', 'opinion'])
        # Skip the header
        next(csv_reader)
        # For each row
        for row in csv_reader:
            # Get the global_score
            global_score = float(row[1])

            # If the random number is less than the global_score
            if global_score < 5:
                # Generate a random opinion
                opinion = random.choice(['I hate it', 'I don\'t like it'])
            # If the random number is greater than the global_score
            else:
                # Generate a random opinion
                opinion = random.choice(['I like it', 'I love it'])
            # Write the row
            csv_writer.writerow([row[0], row[1], row[2], row[3], opinion])
