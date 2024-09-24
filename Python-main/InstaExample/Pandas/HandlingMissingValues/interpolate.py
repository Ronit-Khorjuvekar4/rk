# In pandas, the interpolate() function is used to fill missing data (NaN values) by performing interpolation, 
# which is the process of estimating unknown values within the range of a discrete set of known values. 
# It is commonly used for time series or continuous data.
# DataFrame.interpolate(method='linear', axis=0, limit=None, inplace=False, limit_direction='forward', limit_area=None, downcast=None, **kwargs)

import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, 8, 9],
    'C': [2, 4, 6, np.nan, 10]
}

df = pd.DataFrame(data)

# Describes the interpolation technique to be used
# method : (e.g., 'linear', 'polynomial', 'nearest', 'time' etc).
# print(df.interpolate(method='linear'))


# # You can use the limit parameter to control how many NaNs are filled:
# print(df.interpolate(limit=1))

# Controls the direction in which to fill NaN values.
# 'forward': Fills NaNs in the forward direction.
# 'backward': Fills NaNs in the backward direction.
# 'both': Fills NaNs in both directions.

# print(df.interpolate(limit_direction='forward'))
# print(df.interpolate(limit_direction='backward'))
# print(df.interpolate(limit_direction='both'))


# Type: int, default 0
# Axis along which to interpolate. 0 is for column-wise, and 1 is for row-wise interpolation.
# print(df.interpolate(method='linear',axis=1))
print(df.interpolate(method='linear',axis=0))






