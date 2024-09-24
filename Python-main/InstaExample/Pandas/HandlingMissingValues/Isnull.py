import pandas as pd
import numpy as np

# df.isnull()  :- True if null, else False
# df.notnull() :- True if notnull, else False
# np.nan       :- In Python, NumPy NAN stands for not a number and is defined as a substitute for declaring value which are numerical values that are 
#                 missing values in an array as NumPy is used to deal with arrays in Python and this can be initialized using numpy
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
}

df = pd.DataFrame(data)

print(df.isnull().sum().sum())

print(df.notnull().sum().sum())

