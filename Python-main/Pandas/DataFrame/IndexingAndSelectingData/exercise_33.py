# Using the .loc method, select rows where the Salary is more than 55000 and the employee joined the company in an odd year.
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

emp = (df['salary'] > 55000) & (df['joiningYear'] % 2 == 0)

print(df.loc[emp])