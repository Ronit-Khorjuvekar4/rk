# Create a new column Bonus that is calculated as 
# 20% of Salary for employees with ExperienceYears greater than 8 years, and 10% otherwise.
#
import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR', 'Finance', 'Sales', 'Marketing'],
    'Salary': [60000, 75000, 85000, 90000, 72000, 80000, 62000, 78000, 81000, 95000],
    'JoiningYear': [2010, 2012, 2015, 2018, 2014, 2013, 2016, 2017, 2019, 2020],
    'Age': [29, 35, 40, 38, 31, 36, 27, 33, 39, 42],
    'ExperienceYears': [10, 8, 6, 4, 7, 9, 5, 7, 3, 2]
}

df = pd.DataFrame(data)

df['Bonus'] = np.where(df['ExperienceYears'] > 8, df['Salary'] * 0.2,df['Salary'] * 0.1)



print(df)



