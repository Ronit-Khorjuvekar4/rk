# Create a DataFrame from a List of Dictionaries with Different Keys

import pandas as pd

data = [
    {'A': 1, 'B': 2},
    {'A': 3, 'C': 4},
    {'B': 5, 'C': 6}
]


df = pd.DataFrame(data)

print(df)