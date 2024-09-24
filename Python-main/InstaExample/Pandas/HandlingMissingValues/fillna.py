# fillna() in pandas is used to replace missing values (NaN) with a specified value or method. 
# This function is useful when handling missing data in a DataFrame or Series.

#  Syntax :- DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, np.nan],
    'C': [7, np.nan, np.nan, 10]
}
df = pd.DataFrame(data)

#      A    B     C
# 0  1.0  NaN   7.0
# 1  2.0  2.0   NaN
# 2  NaN  3.0   NaN
# 3  4.0  NaN  10.0

# print( df.fillna(value=0) ) #The value used to fill NaN values. Can be a scalar, dictionary, Series, or DataFrame.

# df.fillna(value=0,inplace=True)
# print(df)

# print( df.fillna(method="ffill") ) # Forward fill — fills with the last valid observation.
# print( df.fillna(method="bfill") ) # Backward fill — fills with the next valid observation.

# print( df.fillna(axis=0,method="bfill") ) # 0 or 'index': Fill values column-wise.
# print( df.fillna(axis=1,method="bfill") ) # 1 or 'columns': Fill values row-wise.

# print( df.fillna(limit=1,method="ffill") ) # Maximum number of consecutive NaN values to fill. It limits how many NaNs in a row can be replaced.

# print( df.fillna(downcast='infer',method="ffill") ) #  convert the filled values into a more memory-efficient data type (such as converting a float column into integers).











