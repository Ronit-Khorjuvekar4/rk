# Write a Pandas program to sort a given Series.

import pandas as pd

s = pd.Series(['100', '200', 'python', '300.12', '400'])

res = s.sort_values()

print(res)