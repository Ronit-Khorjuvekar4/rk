# Create a DataFrame from a Nested Dictionary

import pandas as pd

data = {
    'City A': {'Population': 1000, 'Area': 50},
    'City B': {'Population': 2000, 'Area': 100},
    'City C': {'Population': 3000}
}


df = pd.DataFrame(data)

print(df)