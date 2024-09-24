#  Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

print("Addition\n",series1+series2)

print("Substraction\n",series1-series2)

print("Division\n",series1/series2)

print("Multiplication\n",series1*series2)
