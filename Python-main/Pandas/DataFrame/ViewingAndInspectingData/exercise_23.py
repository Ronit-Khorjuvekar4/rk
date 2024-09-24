# Which method would you use to inspect the first 3 and last 3 rows of the DataFrame simultaneously?
import pandas as pd

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

first_last_rows = pd.concat([df.head(3), df.tail(3)])
print(first_last_rows)


