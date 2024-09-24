# Create a DataFrame with an Existing Index

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
index = ['ID1', 'ID2', 'ID3']

df = pd.DataFrame(data,index=index)

print(data)