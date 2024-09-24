# Extract rows where Education is either 'Bachelor's' or 'PhD' and the City is not 'New York'.
# 
import pandas as pd

data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Eva Martinez', 
             'Fiona Davis', 'George White', 'Hannah Scott', 'Ian Lewis', 'Julia Clark'],
    'Age': [28, 34, 25, 42, 29, 31, 38, 26, 30, 35],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Department': ['HR', 'IT', 'Engineering', 'Marketing', 'Finance', 'IT', 'Engineering', 'Sales', 'HR', 'Finance'],
    'JobTitle': ['Manager', 'Developer', 'Engineer', 'Analyst', 'Accountant', 'Developer', 'Senior Engineer', 'Sales Executive', 'HR Executive', 'Financial Analyst'],
    'ExperienceYears': [5, 8, 3, 12, 4, 6, 15, 2, 1, 9],
    'Education': ['Bachelor\'s', 'Master\'s', 'PhD', 'Master\'s', 'Bachelor\'s', 'PhD', 'Master\'s', 'Bachelor\'s', 'Bachelor\'s', 'Master\'s'],
    'Salary': [55000, 80000, 60000, 75000, 50000, 85000, 90000, 45000, None, 70000]
}

df = pd.DataFrame(data)

emp = (df['Education'].isin(['Bachelor\'s','PhD']) & (df['City'] != 'New York'))

print(df.loc[emp])
