import pandas as pd
import json
from fuzzywuzzy import process

# Load CSV file
csv_file = 'new_geocoded_testimonies-en.csv'  # Replace with your CSV file path
df_csv = pd.read_csv(csv_file)

# Load GeoJSON file
geojson_file = 'SS_Camps_Definitive.json'  # Replace with your GeoJSON file path
with open(geojson_file, 'r') as file:
    geojson_data = json.load(file)

# Normalize and split campsite names in the CSV
def normalize_and_split(names):
    # Split by common delimiters and strip whitespace
    delimiters = [',', ';', ':']
    for delimiter in delimiters:
        names = names.replace(delimiter, ',')
    return [name.strip() for name in names.split(',')]

df_csv['Normalized_Names'] = df_csv['Camps'].apply(normalize_and_split)

# Extract camp names from GeoJSON properties
geojson_camp_names = {}

for feature in geojson_data:
    campname = (feature['properties']['MAIN']).strip()
    geojson_camp_names[campname] = feature["geometry"]["coordinates"]

# Function to find best match
def find_best_match(names):
    matches = []
    for name in names:
        match, score = process.extractOne(name, geojson_camp_names.keys())
        if score > 90:
            # print(score, name, match)
            matches.append(match)
    
    return matches

# Apply the matching function
df_csv['Best_Match'] = df_csv['Normalized_Names'].apply(find_best_match)

df_csv = df_csv.reset_index()  # make sure indexes pair with number of rows

new_array = []

for index, row in df_csv.iterrows():
    for entry in row['Best_Match']:
        new_row = row.copy()
        new_row["single_match"] = entry
        new_array.append(new_row)


# Save the merged results
output_file = 'merged_campsites_withloc.csv'  # Replace with your desired output file name
pd.DataFrame(new_array).to_csv(output_file, index=False)
