# The replace() function in Pandas is used to replace specific values in a DataFrame or Series with new values. 
# It is versatile and allows you to replace values based on conditions such as single values, lists, or regular expressions.

# DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method=None)

import pandas as pd
import numpy as np

# Creating the dataset
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, np.nan, 52000],
    'ExperienceYears': [5, 4, np.nan, 7, 1],
    'Gender': ['F', None, 'M', None, None],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, 'Phoenix'],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', np.nan]
}

df = pd.DataFrame(data)
# print(df)

# print( df.replace(to_replace='M', value='Male') ) # Replacing a single value

# # If inplace=True, the operation will modify the original DataFrame without returning a new one. 
# # If False, the operation returns a new DataFrame with the replacements.
# df.replace(to_replace='M', value='Male', inplace=False)
# print(df)

# # df.replace(to_replace=r'^New.*', value='NY City', regex=True)
# print( df.replace(to_replace=r'^New.*', value='NY City', regex=True) )

# #This parameter is used to fill forward or backward. You can set the method to 'ffill' (forward fill) or 'bfill' (backward fill).
# print( df.replace(to_replace='IT', method='ffill') )
# print( df.replace(to_replace=np.nan, method='bfill') )

# # Maximum size gap to forward or backward fill.
print( df.replace(np.nan, None, limit=2, method='ffill') )




