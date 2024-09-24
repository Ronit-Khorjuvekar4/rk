# Select all employees who joined between 2016 and 2018, and sort them by Salary in descending order.
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

emp = df[df['joiningYear'].between(2016,2018)].sort_values(by='salary',ascending=False)
print(emp)

employees_2016_2018_sorted = df[(df['JoiningYear'] >= 2016) & (df['JoiningYear'] <= 2018)].sort_values(by='Salary', ascending=False)
print(employees_2016_2018_sorted)