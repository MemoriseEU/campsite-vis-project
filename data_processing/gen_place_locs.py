import pandas as pd
import json
from fuzzywuzzy import process
import math

# Load CSV file
csv_file = 'merged_campsites_new.csv'  # Replace with your CSV file path
df_csv = pd.read_csv(csv_file)

place_ids = {}
place_locs = {}

df = df_csv.reset_index()  # make sure indexes pair with number of rows

for index, row in df_csv.iterrows():
    if str(row['born_place_id']) not in place_locs and not math.isnan(row["born_Longitude"]):
        place_locs[str(row['born_place_id'])] = {"id": str(row['born_place_id']),"longitude": row["born_Longitude"], "latitude": row["born_Latitude"], "label": row["Place_of_birth"]}

print(place_locs)

# Save the merged results
output_file = 'locs.csv'  # Replace with your desired output file name
pd.DataFrame(place_locs.values()).to_csv(output_file, index=False)
