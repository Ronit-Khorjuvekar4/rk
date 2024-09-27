# Create a new column JobSatisfaction which assigns values from 1 to 5 (randomly) 
# for each employee based on a predefined dictionary with employee names and scores.
#
import pandas as pd
import numpy as np

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


name_to_score = {
    'Alice': 4,
    'Bob': 3,
    'Charlie': 5,
    'David': 2,
    'Eve': 1
}


df['JobSatisfaction'] = np.nan

# Assign values based on the dictionary using `loc`
for name, score in name_to_score.items():
    df.loc[df['Name'] == name, 'JobSatisfaction'] = score


df['JobSatisfaction'] = df['Name'].map(name_to_score)

print(df)





