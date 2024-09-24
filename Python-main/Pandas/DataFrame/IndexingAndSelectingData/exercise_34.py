# Find the employees who are in the 
# HR department and have a salary either equal to or lower than the average salary of all employees in the DataFrame.
import pandas as pd

data = {
    'employeeid': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 55000, 70000, 90000],
    'joiningYear': [2015, 2016, 2017, 2018, 2019],
    'age': [25, 28, 30, 35, 22]
}

df = pd.DataFrame(data)
ep = df['salary'].sum() / df['salary'].count()
emp = (df['department'] == 'HR') & (df['salary'] <= ep)

print(df[emp])

average_salary = df['salary'].mean()
hr_low_salary = df[(df['department'] == 'HR') & (df['salary'] <= average_salary)]
print(hr_low_salary)