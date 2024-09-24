# Create a DataFrame from a Dictionary of NumPy Arrays

import pandas as pd
import numpy as np

data = {
    'A': np.array([1, 2, 3]),
    'B': np.array([4, 5, 6])
}

df = pd.DataFrame(data)

print(df)