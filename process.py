import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

data = pd.read_json("/content/entries.json")
df = data['entries'].apply(pd.Series)