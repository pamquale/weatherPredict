import pandas as pd

# Load datasets into dataframes
df1 = pd.read_csv('data/comp_datasets_train/solution_format.csv')
df2 = pd.read_csv('reformatted_file.csv')

# Merge dataframes on 'date' column
df_merged = df1.merge(df2, on='date', suffixes=('_old', ''))

# Overwrite 'label' in df1 with updated values
df1['label'] = df_merged['label']

# Save the updated Dataset 1
df1.to_csv('dataset1_updated.csv', index=False)
