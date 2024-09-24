# Create a DataFrame from a 1D NumPy Array

import pandas as pd
import numpy as np

data = np.array([10, 20, 30, 40, 50])

df = pd.DataFrame(data)

print(df)
