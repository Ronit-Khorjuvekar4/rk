# Which method would you use to find the 25th percentile of the Age column?
import pandas as pd
import numpy as np

# Creating the dataset
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 55000, 70000, 52000, 59000, 62000, 50000, 61000, 70000],
    'JoiningYear': [2015, 2016, 2017, 2018, 2019, 2020, 2017, 2015, 2018, 2016],
    'Age': [25, 28, 30, 35, 22, 40, 26, 29, 32, 27],
    'ExperienceYears': [5, 4, 3, 7, 1, 15, 2, 6, 10, 4],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'F'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', 'Masters', 'PhD', 'Bachelors', 'Bachelors', 'Masters', 'PhD']
}

df = pd.DataFrame(data)

age_25th_percentile = df['Age'].quantile(0.25)
print(age_25th_percentile)



