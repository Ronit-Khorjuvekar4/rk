# The dropna() function in pandas is used to remove missing values (NaNs) from a DataFrame or Series.
# syntax :- DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4,np.nan],
    'B': [5, np.nan, np.nan, 8,np.nan],
    'C': [9, 10, 11, 12,np.nan]
}

#     A    B   C
# 0  1.0  5.0   9
# 1  2.0  NaN  10
# 2  NaN  NaN  11
# 3  4.0  8.0  12
# 4  NaN  NaN  Nan

df = pd.DataFrame(data)

#oko

<<<<<<< HEAD
# df.dropna(inplace=True)
=======
df.dropna(inplace=True)
>>>>>>> 84eafc280b5340dc44e2a85dbb896a59cd40d2bd
# print(df)

# print(df.dropna(axis=0),'\n') # axis=0 or axis='index': Drop rows with missing values (default).
# print(df.dropna(axis=1)) # axis=1 or axis='columns': Drop columns with missing values.

# print(df.dropna(how="any"),'\n') # how='any': Drop the row or column if any of the values are missing (default).
# print(df.dropna(how="all")) # how='all': Drop the row or column only if all of the values are missing.

# print(df.dropna(thresh=3)) # Requires that many non-NaN values.

print(df.dropna(subset=['A','B'])) # Specifies which columns to consider for dropping rows.




