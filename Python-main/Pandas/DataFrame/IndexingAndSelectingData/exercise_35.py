# Select all columns for employees who do not belong to the HR department, 
# and either their Salary is above the median salary or they joined before 2017.
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

emp = (df['department'] != 'HR') & ((df['salary'] > df['salary'].median()) | (df['joiningYear'] < 2017))

print(df[emp])