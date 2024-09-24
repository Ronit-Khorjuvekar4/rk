# Create a DataFrame from a Multi-dimensional NumPy Array

import pandas as pd
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = ['Row1', 'Row2', 'Row3']
columns = ['A', 'B', 'C']

df = pd.DataFrame(data,columns=columns,index=rows)

print(df)
