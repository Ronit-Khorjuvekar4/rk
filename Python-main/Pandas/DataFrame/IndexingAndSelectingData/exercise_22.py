# Retrieve the Name, Age, and Salary of the employee who has the third highest salary in the DataFrame.
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

print(df.sort_values(by='salary',ascending=False).loc[:,['name', 'age', 'salary']].head(3).tail(1))
print(df.sort_values(by='salary',ascending=False).head(3).tail(1))
print(df.nlargest(3, 'salary').iloc[2][['name', 'age', 'salary']])
print(df.nlargest(3,'salary').loc[2:,['name', 'age', 'salary']])