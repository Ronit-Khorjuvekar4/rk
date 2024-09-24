#  Create a DataFrame from a List of Lists

import pandas as pd

data = [
    [1, 'Apple', 0.5],
    [2, 'Banana', 0.3],
    [3, 'Cherry', 0.2]
]
columns = ['ID', 'Fruit', 'Price']

df = pd.DataFrame(data,columns=columns)

print(df)