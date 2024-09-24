# Create a new DataFrame that excludes the name and department columns and select only those rows where the salary is within one 
# standard deviation of the mean salary.

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

df_excluded = df.drop(columns=['name', 'department'])
mean_salary = df_excluded['salary'].mean()
std_salary = df_excluded['salary'].std()

within_one_std = df_excluded[(df_excluded['salary'] >= mean_salary - std_salary) & 
                             (df_excluded['salary'] <= mean_salary + std_salary)]
print(within_one_std)
