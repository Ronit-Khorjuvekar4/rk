# Select the Name and Department of the employee with the longest tenure in the company (based on JoiningYear).
import pandas as pd
import datetime

data = {
    'employeeid': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 55000, 70000, 52000],
    'joiningYear': [2015, 2016, 2017, 2018, 2019],
    'age': [25, 28, 30, 35, 22]
}

df = pd.DataFrame(data)

emp =  datetime.datetime.now().year - df['joiningYear']

print(df.loc[emp.idxmax(),['name','department']])

longest_tenure = df.loc[df['joiningYear'].idxmin(), ['name', 'department']]
print(longest_tenure)
