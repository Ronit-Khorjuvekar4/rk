# Create a DataFrame from an Array with Custom Column Names

import pandas as pd
import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
columns = ['Col1', 'Col2']

df = pd.DataFrame(data,columns=columns)

print(df)
