# Given a file called sentiment-tourist-atraction_v2.csv
# With five columns: id, global_score, agregate_count, tourist-atraction, opinion
# Create an script which analyses the human opinions on the last column
# Create a new file called sentiment-tourist-atraction_v3.csv
# With the same structure as the input file plus an extra column called sentiment
# The sentiment column should be a number between 1 and 10 based on the positivism of the opinion
# Use sentimnet analysis to generate the sentiment column
# The sentiment column should be generated based on the opinion column
# The sentiment column should be generated using the TextBlob library
# The sentiment column should be generated using the sentiment.polarity property
# The sentiment column should be generated using the sentiment.subjectivity property
# The sentiment column should be generated using the sentiment_assessments property


import csv
from textblob import TextBlob

# Read the csv file
with open('sentiment-tourist-atraction_v2.csv', 'r', encoding='utf8') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')

    # Skip the header
    next(csv_reader)

    # Open a new csv file
    with open('sentiment-tourist-atraction_v3.csv', 'w', newline='', encoding='utf8') as csv_file:

        csv_writer = csv.writer(csv_file, delimiter=';')

        # Write the header
        csv_writer.writerow(['id', 'global_score', 'agregate_count', 'tourist-atraction', 'opinion', 'sentiment'])

        # For each row
        for row in csv_reader:

            # Get the opinion
            opinion = row[4]

            # Create a TextBlob object
            text_blob = TextBlob(opinion)

            # Get the sentiment
            sentiment = text_blob.sentiment.polarity

            # Write the row
            csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], sentiment])

    # close the file
    csv_file.close()


# With the result file generate a dispersion graph of the sentiment column and global_score column
# The dispersion graph should be generated using the matplotlib library
# The dispersion graph should be generated using the scatter function
# The dispersion graph should be generated using the show function
# The dispersion graph should be generated using the savefig function
# The dispersion graph should be generated using the title function
# The dispersion graph should be generated using the xlabel function
# The dispersion graph should be generated using the ylabel function
# The dispersion graph should be generated using the legend function
# The dispersion graph should be generated using the tight_layout function
# The dispersion graph should be generated using the figure function
# The dispersion graph should be generated using the subplots function
# The dispersion graph should be generated using the set_size_inches function
# The dispersion graph should be generated using the set_facecolor function
# The dispersion graph should be generated using the set_alpha function
# The dispersion graph should be generated using the set_edgecolor function
# The dispersion graph should be generated using the set_linewidth function
# The dispersion graph should be generated using the set_linestyle function


import matplotlib.pyplot as plt

# Read the csv file
with open('sentiment-tourist-atraction_v3.csv', 'r', encoding='utf8') as csv_file:
    
        csv_reader = csv.reader(csv_file, delimiter=';')
    
        # Skip the header
        next(csv_reader)
    
        # Create the lists
        global_score = []
        sentiment = []
    
        # For each row
        for row in csv_reader:
    
            # Get the global_score
            global_score.append(float(row[1]))
    
            # Get the sentiment
            sentiment.append(float(row[5]))
    
        # Create the figure
        fig, ax = plt.subplots()
    
        # Set the figure size
        fig.set_size_inches(16, 9)
    
        # Set the background color
        ax.set_facecolor('#f6f5f7')
    
        # Set the figure title
        fig.suptitle('Sentiment vs Global Score', fontsize=20)
    
        # Set the x axis label
        plt.xlabel('Global Score', fontsize=18)
    
        # Set the y axis label
        plt.ylabel('Sentiment', fontsize=18)
    
        # Set the scatter plot
        plt.scatter(global_score, sentiment, s=100, c='#ff7f0e', alpha=0.5, edgecolors='black', linewidths=1, linestyle='solid')
    
        # Set the legend
        plt.legend(['Sentiment vs Global Score'])
    
        # Set the tight layout
        plt.tight_layout()
    
        # Save the figure
        plt.savefig('sentiment-vs-global-score.png')
    
        # Show the figure
        plt.show()
    
        # Close the file
        csv_file.close()


# With the results generate a graph with the average sentiment per tourist-atraction
# The graph should be generated using the matplotlib library
# The graph should be generated using the bar function
# The graph should be generated using the show function


import matplotlib.pyplot as plt

# Read the csv file
with open('sentiment-tourist-atraction_v3.csv', 'r', encoding='utf8') as csv_file:
        
            csv_reader = csv.reader(csv_file, delimiter=';')
        
            # Skip the header
            next(csv_reader)
        
            # Create the lists
            tourist_atraction = []
            sentiment = []
        
            # For each row
            for row in csv_reader:
        
                # Get the tourist_atraction
                tourist_atraction.append(row[3])
        
                # Get the sentiment
                sentiment.append(float(row[5]))
        
            # Create the figure
            fig, ax = plt.subplots()
        
            # Set the figure size
            fig.set_size_inches(16, 9)
        
            # Set the background color
            ax.set_facecolor('#f6f5f7')
        
            # Set the figure title
            fig.suptitle('Average Sentiment per Tourist Atraction', fontsize=20)
        
            # Set the x axis label
            plt.xlabel('Tourist Atraction', fontsize=18)
        
            # Set the y axis label
            plt.ylabel('Average Sentiment', fontsize=18)
        
            # Set the bar plot
            plt.bar(tourist_atraction, sentiment, color='#ff7f0e')
        
            # Set the legend
            plt.legend(['Average Sentiment per Tourist Atraction'])
        
            # Set the tight layout
            plt.tight_layout()
        
            # Save the figure
            plt.savefig('average-sentiment-per-tourist-atraction.png')
        
            # Show the figure
            plt.show()
        
            # Close the file
            csv_file.close()


            