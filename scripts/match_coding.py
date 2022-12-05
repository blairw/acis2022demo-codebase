import yaml
import pandas as pd

all_codes = []
with open("AllCodes.yml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)
    for key, value in data_loaded.items():
        value["code_id"] = key
        all_codes.append(value)

df_all_codes = pd.DataFrame(all_codes)
col_code_id = df_all_codes.pop("code_id")
df_all_codes.insert(0, "code_id", col_code_id)

print(df_all_codes)

