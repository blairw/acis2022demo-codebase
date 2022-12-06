import yaml
import pandas as pd

quote_utilisations = {}
all_codes = []
with open("AllCodes.yml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)
    for code_id, value in data_loaded.items():
        # Store code_id
        value["code_id"] = code_id
        
        # Register the quote utilisation
        for this_quote in value["quotes"]:
            if this_quote in quote_utilisations.keys():
                quote_utilisations[this_quote].append(code_id)
            else:
                quote_utilisations[this_quote] = [code_id]
                    
        # Save item into list
        all_codes.append(value)

df_all_codes = pd.DataFrame(all_codes)
col_code_id = df_all_codes.pop("code_id")
df_all_codes.insert(0, "code_id", col_code_id)

df_quotes = pd.read_csv("./outputs/01-extracted-quotes/unified_quotes.csv")
for quote_id in quote_utilisations.keys():
    df_quotes.loc[df_quotes["quote_id"] == quote_id, "utilisations"] = ", ".join(quote_utilisations[quote_id])

df_quotes.sort_values(by=["utilisations"], inplace=True, na_position='first')

df_quotes.to_csv("./outputs/02-coding/df_quotes.csv", index=False)
df_quotes.to_html("./outputs/02-coding/df_quotes.html", index=False)
df_all_codes.to_csv("./outputs/02-coding/df_all_codes.csv", index=False)
df_all_codes.to_html("./outputs/02-coding/df_all_codes.html", index=False)


