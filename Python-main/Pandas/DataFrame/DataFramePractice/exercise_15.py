# Create a DataFrame from a Dictionary with Missing Data

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, None, 6],
    'C': [7, 8, None]
}

df = pd.DataFrame(data)

print(df)