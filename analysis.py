import json
import pandas as pd

# Replace 'your_file_path.json' with the actual path to your JSON file
json_file_path = 'SS_Camps_Definitive.json'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    # Load the JSON data
    json_data = json.load(file)

# Display the loaded JSON data

props = [element["properties"] for element in json_data]

print(props)

df = pd.DataFrame(props)

ar = [element.split(",") for element in df.PRISONERS.unique()]

print(ar)