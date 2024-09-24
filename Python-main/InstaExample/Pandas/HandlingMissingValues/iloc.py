# # - iloc in Pandas allows you to retrieve,filter, 
# # or update, data in a DataFrame using their integer 
# # positions (index numbers). It allows you to 
# # select data based on numerical indices, 
# # which makes it useful when you don’t know the labels -

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 40, 22],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)

# # # Syntax :- df.iloc[ : , [] ]

# # Get first 3 rows of column "Name"
# # print(df.iloc[:3,[0]])

# # Get first 3 rows of column "Name" and "Age"
# # print(df.iloc[:3,[0,1]])

# # Get all the data
# print(df.iloc[:,])

s = "iphone 15"

print(s[:3])

