# Create a new column PositionLevel which is 'Junior' for Salary less than 60000, 
# 'Mid' for Salary between 60000 and 70000, and 'Senior' for Salary above 70000.
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

df.loc[:,'PositionLevel'] = pd.cut(df['Salary'],bins=[-float('inf'),60000,70000,float('inf')],labels=['Junior','Mid','Senior'])

print(df)

