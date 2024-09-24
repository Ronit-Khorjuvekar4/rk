# Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)