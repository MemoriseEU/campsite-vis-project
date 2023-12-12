import os
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import json

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Folder containing the text files
folder_path = './text-en'  # Replace with your folder path

# Initialize a Counter object to count word occurrences
word_counts = Counter()

# English stop words
stop_words = set(stopwords.words('english'))

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Tokenize and normalize the text
            tokens = word_tokenize(text)
            normalized_tokens = [word.lower() for word in tokens if word.isalpha()]
            
            # Remove stop words
            words = [word for word in normalized_tokens if word not in stop_words]
            
            # Update word counts
            word_counts.update(words)

# Convert the Counter object to a list of dictionaries
words_data = [{'word': word, 'size': count} for word, count in word_counts.items()]

# Save to JSON
output_json = 'word_counts.json'  # Replace with your desired output file name
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(words_data, f, ensure_ascii=False, indent=4)

# # Convert the Counter object to a DataFrame
# df_word_counts = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])

# # Sort by count in descending order
# df_word_counts.sort_values(by='Count', ascending=False, inplace=True)

# # Save to CSV
# output_csv = 'word_counts.csv'  # Replace with your desired output file name
# df_word_counts.to_csv(output_csv, index=False)
