# How do you drop rows where the Name column has missing values?
import pandas as pd
import numpy as np

# Creating the dataset with missing values
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eva', 'Frank', np.nan, 'Hannah', 'Ian', 'Jane'],
    'Department': ['HR', 'IT', np.nan, 'IT', 'HR', 'Finance', 'IT', np.nan, 'Finance', 'IT'],
    'Salary': [50000, 60000, np.nan, 70000, 52000, np.nan, 62000, 50000, 61000, 70000],
    'JoiningYear': [2015, 2016, 2017, 2018, np.nan, 2020, 2017, 2015, 2018, 2016],
    'Age': [25, 28, 30, 35, 22, np.nan, 26, 29, np.nan, 27],
    'ExperienceYears': [5, np.nan, 3, 7, 1, 15, 2, 6, 10, 4],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', np.nan, 'F', 'M', 'F'],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', np.nan],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', 'Masters', 'PhD', np.nan, 'Bachelors', 'Masters', 'PhD']
}

df = pd.DataFrame(data)

df_dropped_name = df.dropna(subset=['Name'])
print(df_dropped_name)

