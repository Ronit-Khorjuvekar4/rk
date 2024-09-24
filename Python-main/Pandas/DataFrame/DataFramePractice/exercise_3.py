# Create a DataFrame from a List of Tuples

import pandas as pd

data = [
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 35, 'Chicago')
]
columns = ['Name', 'Age', 'City']

df = pd.DataFrame(data,columns=columns)

print(df)
