# Create a DataFrame from a Dictionary with Index and Columns Specified

import pandas as pd

data = {
    'Math': [80, 90, 70],
    'English': [85, 95, 75]
}
index = ['Student1', 'Student2', 'Student3']
columns = ['Math', 'English']

df = pd.DataFrame(data,columns=columns,index=index)

print(df)