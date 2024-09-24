# Create a DataFrame with Index from a Dictionary

import pandas as pd

data = {
    'Product': ['A', 'B', 'C'],
    'Price': [10, 20, 30]
}
index = ['Store 1', 'Store 2', 'Store 3']

df = pd.DataFrame(data,index=index)

print(df)
