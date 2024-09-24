# Select the 'ID', 'Name', and 'Joining Date' of employees 
# who joined in 2020 and their 'Performance Score' is exactly 10.
# 
import pandas as pd

data = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack', 'Karl', 'Liam', 'Mona', 'Nina', 'Oscar'],
    'Department': ['HR', 'IT', 'Sales', 'Finance', 'Marketing', 'IT', 'HR', 'Finance', 'Marketing', 'Sales', 'IT', 'HR', 'Marketing', 'Finance', 'Sales'],
    'Salary': [55000, 72000, 45000, 68000, 52000, 71000, 48000, 64000, 58000, 46000, 75000, 50000, 62000, 66000, 43000],
    'JoiningDate': ['2018-03-15', '2020-06-20', '2017-11-01', '2019-01-05', '2016-05-10', '2020-07-22', '2018-09-14', '2019-11-25', '2017-02-28', '2015-08-30', '2022-03-12', '2016-12-05', '2019-06-10', '2020-04-18', '2017-10-20'],
    'PerformanceScore': [8, 9, 6, 7, 8, 10, 5, 6, 7, 4, 9, 5, 6, 8, 3]
}

df = pd.DataFrame(data)

datee = pd.to_datetime(df['JoiningDate'])

yearr = datee.dt.year

performanceScore = (df['PerformanceScore'] == 10) & (yearr == 2020)

print(df.loc[performanceScore])
