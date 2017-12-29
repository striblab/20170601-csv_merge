import pandas as pd

a = pd.read_csv("CSV1.csv")
b = pd.read_csv("CSV2.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='COMMONHEADER')
merged.to_csv("MERGED_FILE.csv", index=False)