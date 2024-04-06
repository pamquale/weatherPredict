import pandas as pd
import csv

# Load datasets into dataframes
df1 = pd.read_csv('data/comp_datasets_train/solution_format.csv')
df2 = pd.read_csv('newshi/region_A_test.csv')

# Create a dictionary where key is the date and value is the order in df2
order_dict = {k: v for v, k in enumerate(df2['date'])}

# Create a new column in df1 called 'order' using the 'date' column mapped to the order_dict
df1['order'] = df1['date'].map(order_dict)

# Sort df1 by this 'order' column
df1.sort_values('order', inplace=True)

# Drop the 'order' column as it's not needed anymore
df1.drop('order', axis=1, inplace=True)

# Save the updated Dataset 1
df1.to_csv('data/comp_datasets_train/solution_format.csv', index=False, quoting=csv.QUOTE_ALL)