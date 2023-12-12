import pandas as pd
import json
from fuzzywuzzy import process

# Load CSV file
csv_file = 'merged_campsites.csv'  # Replace with your CSV file path
df_csv = pd.read_csv(csv_file)

place_ids = {}
place_locs = {}

def create_id(name):
    global place_ids

    if name != "unknown": 
        if name not in place_ids:
            place_ids[name] = len(place_ids) + 1

        return place_ids[name]
    else:
        return "unknown"

    
df_csv['born_place_id'] = df_csv['Place_of_residence'].apply(create_id)

# Save the merged results
output_file = 'merged_campsites_new.csv'  # Replace with your desired output file name
df_csv.to_csv(output_file, index=False)
