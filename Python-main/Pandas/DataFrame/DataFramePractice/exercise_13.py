# Create a DataFrame from an Indexed List of Lists

import pandas as pd

data = [
    [10, 20, 30],
    [40, 50, 60]
]
index = ['Row1', 'Row2']
columns = ['A', 'B', 'C']

df = pd.DataFrame(data,index=index,columns=columns)

print(df)
