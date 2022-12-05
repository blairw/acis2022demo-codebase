import os
import pandas as pd
import hashlib

JSON_DIR = "./outputs/01-extracted-quotes/"


# Adapted from https://www.geeksforgeeks.org/md5-hash-python/
def generate_unique_hash(row):
    concatted_string = row["coded_file"] + "_" + str(row["start_xy"][0]) + "_" + str(row["start_xy"][1])
    return hashlib.md5(concatted_string.encode()).hexdigest()


all_files = os.listdir(JSON_DIR)
json_files = []
for f in all_files:
    if f[-5:] == '.json':
        json_files.append(f[0:-5])

datasets = []
for f in json_files:
    this_json = pd.read_json(JSON_DIR + f + ".json")

    # Unique ID
    this_json.rename(columns = {'text': 'quoted_text'}, inplace = True)
    this_json.rename(columns = {'contents': 'open_coding'}, inplace = True)

    # Identify coded file first
    this_json["coded_file"] = f

    # Remove unnecessary cols
    for col_to_remove in ["type", "prior_outline"]:
        if col_to_remove in this_json:
            this_json.pop(col_to_remove)

    # Calculate unique hash
    this_json["quote_id"] = this_json.apply(lambda row: generate_unique_hash(row), axis=1)
    
    # Reorder
    col_unique_hash = this_json.pop("quote_id") 
    col_coded_file = this_json.pop("coded_file")
    this_json.insert(0, "quote_id", col_unique_hash)
    this_json.insert(1, "coded_file", col_coded_file)
    
    datasets.append(this_json)

pd_unified = pd.concat(datasets)
pd_unified.to_csv(JSON_DIR + "unified_quotes.csv", index=False)
pd_unified.to_html(JSON_DIR + "unified_quotes.html", index=False)
