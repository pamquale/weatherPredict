import pandas as pd
import csv

df = pd.read_csv('dataset1_updated.csv', header=None)  # Load CSV (assuming no header)
df.to_csv('reformatted_file2.csv', index=False, header=False, quoting=csv.QUOTE_ALL)
