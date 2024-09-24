# Using the .loc method, retrieve all rows where the Department is IT, 
# and the Salary is greater than or equal to 60000, but only return the EmployeeID, Name, and Salary columns.
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

listt = ['name','employeeid','salary']
emp = (df['department'] == "IT") & (df['salary'] >= 60000)

print(df.loc[emp,listt])