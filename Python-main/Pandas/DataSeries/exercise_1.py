# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

import pandas as pd

arr = [1,2,3,4]

series = pd.Series(arr)

print(series)