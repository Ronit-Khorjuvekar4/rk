#  Create a DataFrame from a Dictionary of Series

import pandas as pd

data = {
    'Population': pd.Series([1000, 2000, 3000], index=['City A', 'City B', 'City C']),
    'Area': pd.Series([50, 100, 150], index=['City A', 'City B', 'City D'])
}

df = pd.DataFrame(data)

print(df)
