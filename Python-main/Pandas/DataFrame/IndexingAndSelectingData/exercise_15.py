# Select the rows of the DataFrame where EmployeeID is either 102 or 105.

import pandas as pd

data = {
    'employeeid': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 55000, 70000, 52000],
    'joiningYear': [2015, 2016, 2017, 2018, 2019],
    'age': [25, 28, 30, 35, 22]
}

df = pd.DataFrame(data)

emp = df[(df['employeeid'] == 102) | (df['employeeid'] == 105)]
emp1 = df[df['employeeid'].isin([102,105])]

print(emp)
print(emp1)
