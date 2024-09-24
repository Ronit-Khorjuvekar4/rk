# Write a Pandas program to add some data to an existing Series.

import pandas as pd

s = pd.Series(['100', '200', 'python', '300.12', '400'])

new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=False)

print(new_s)