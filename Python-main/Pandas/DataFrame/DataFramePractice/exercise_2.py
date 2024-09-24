# Create a DataFrame from a List of Dictionaries

import pandas as pd

data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

df = pd.DataFrame(data)

print(df)
