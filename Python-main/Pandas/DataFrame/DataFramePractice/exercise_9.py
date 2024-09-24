#  Create a DataFrame with Specific Data Types

import pandas as pd

data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Score': [88.5, 92.3]
}
dtypes = {'Name': 'str', 'Age': 'int32', 'Score': 'float64'}

df = pd.DataFrame(data)

print(df)