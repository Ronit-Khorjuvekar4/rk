# Select the Name of the second youngest employee in the IT department.
import pandas as pd

data = {
    'employeeid': [101, 102, 103, 104, 105,106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','marine'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR','IT'],
    'salary': [50000, 60000, 55000, 70000, 52000,90888],
    'joiningYear': [2015, 2016, 2017, 2018, 2019,2020],
    'age': [25, 28, 30, 35, 22,30]
}

df = pd.DataFrame(data)

emp = df['department'] == 'IT'

print(df[emp].sort_values(by='age',ascending=False).iloc[-2,1])

second_youngest_it = df[df['department'] == 'IT'].nsmallest(2, 'age').iloc[1]['name']
print(second_youngest_it)
