import pandas as pd

# Assuming you have a CSV file with a column named 'Year'
# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file = './testimonies-en.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file, sep="\t")

# Add a new column with the format 'YYYY-01-01'
df['First_of_January'] = df['Year_of_birth'].apply(lambda x: f"{x}-01-01")

# Save the updated DataFrame back to a CSV file
# Replace 'output_csv_file.csv' with the desired output file name
df.to_csv('new_testimonies-en.csv', index=False)