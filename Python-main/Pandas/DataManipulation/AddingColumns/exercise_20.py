# Create a new column DepartmentRank which assigns 
# rank 1 to 'HR', 2 to 'IT', and 3 to 'Finance' based 
# on Salary in ascending order.
#
import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane', 'Kyle', 'Laura', 'Mona', 'Nate', 'Olivia'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 70000, 52000, 61000, 72000, 66000, 63000, 59000, 67000, 64000, 71000, 68000, 55000, 62000],
    'JoiningYear': [2015, 2016, 2017, 2018, 2019, 2020, 2017, 2015, 2018, 2016, 2019, 2020, 2017, 2018, 2016],
    'Age': [25, 28, 30, 35, 22, 34, 26, 29, 27, 33, 31, 30, 29, 32, 30],
    'City': ['New York', 'Los Angeles', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Chicago', 'Miami', 'San Francisco', 'Seattle', 'Austin', 'Denver', 'Boston'],
}

df = pd.DataFrame(data)

df['DepartmentRank'] = df.groupby('Department')['Salary'].rank(method='dense')


print(df)


