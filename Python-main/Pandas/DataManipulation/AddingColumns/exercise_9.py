# Create a new column PerformanceScore and fill it with 'A' 
# for employees whose ExperienceYears is more than 7, 'B' for 4 to 7, and 'C' for less than 4.
#
import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 70000, 52000, 61000, 72000, 66000, 63000, 59000, 67000],
    'JoiningYear': [2015, 2016, 2017, 2018, 2019, 2020, 2017, 2015, 2018, 2016],
    'Age': [25, 28, 30, 35, 22, 34, 26, 29, 27, 33]
}

df = pd.DataFrame(data)

df.loc[:,'ExperienceYears'] = 2024 - df['JoiningYear']

def func(x):
    if(x > 7):
        return 'A'
    elif((x > 4) and (x <= 7)):
        return 'B'
    elif((x <= 4)):
        return 'C'

# df.loc[:,'PerformanceScore'] = df['ExperienceYears'].apply(func)

df['PerformanceScore'] = pd.cut(df['ExperienceYears'], bins=[-float('inf'), 3, 7, float('inf')], labels=['C', 'B', 'A'])


print(df)

