# - loc in Pandas is a function used to select 
# and access rows and columns in a DataFrame 
# by their labels (names). It allows you to 
# filter, update, or retrieve data based on 
# row and column names -

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Syntax :- df.loc[ : , ]

# Get first 3 rows of column "Name"
print(df.loc[:2,['Name']])

# Get first 3 rows of column "Name" and "Age"
# print(df.loc[:2,['Name','Age']])

# Get all the data
# print(df.loc[:,])


