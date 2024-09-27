# Create a new column DepartmentCode by mapping 'HR' to 1, 'IT' to 2, and 'Finance' to 3.
# 
import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 70000, 52000, 61000, 72000, 66000, 63000, 59000, 67000],
    'JoiningYear': [2015, 2016, 2017, 2018, 2019, 2020, 2017, 2015, 2018, 2016],
    'Age': [25, 28, 30, 35, 22, 34, 26, 29, 27, 33]
}

df = pd.DataFrame(data)

deptCode = {'HR':1,'IT':2,'Finance':3}

df.loc[:,'DepartmentCode'] = df['Department'].map(deptCode)

print(df)

