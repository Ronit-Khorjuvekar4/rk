# Add a new column called SeniorityLevel that classifies employees into 
# 'Junior', 'Mid', or 'Senior' based on their ExperienceYears (e.g., <5 years = 'Junior', 5-10 years = 'Mid', >10 years = 'Senior').
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

import numpy as np

# Define conditions and corresponding choices for SeniorityLevel
conditions = [
    df['ExperienceYears'] < 5,
    (df['ExperienceYears'] >= 5) & (df['ExperienceYears'] <= 10),
    df['ExperienceYears'] > 10
]

choices = ['Junior', 'Mid', 'Senior']

# Use np.select to assign the values based on the conditions
df['SeniorityLevel'] = np.select(conditions, choices, default='Unknown')




print(df)



