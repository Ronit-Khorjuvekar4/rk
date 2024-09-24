# Create a DataFrame from a Mixed Data Dictionary

import pandas as pd

data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'IsStudent': [True, False]
}

df = pd.DataFrame(data)

print(df)