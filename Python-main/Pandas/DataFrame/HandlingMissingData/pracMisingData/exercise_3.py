# What method would you use to drop rows with any missing values?
import pandas as pd
import numpy as np

# Creating the dataset with missing values
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,np.nan],
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eva', 'Frank', np.nan, 'Hannah', 'Ian', 'Jane',np.nan],
    'Department': ['HR', 'IT', np.nan, 'IT', 'HR', 'Finance', 'IT', np.nan, 'Finance', 'IT',np.nan],
    'Salary': [50000, 60000, np.nan, 70000, 52000, np.nan, 62000, 50000, 61000, 70000,np.nan],
    'JoiningYear': [2015, 2016, 2017, 2018, np.nan, 2020, 2017, 2015, 2018, 2016,np.nan],
    'Age': [25, 28, 30, 35, 22, np.nan, 26, 29, np.nan, 27,np.nan],
    'ExperienceYears': [5, 4, 3, 7, 1, 15, 2, 6, 10, 4,np.nan],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', np.nan, 'F', 'M', 'F',np.nan],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', np.nan,np.nan],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', 'Masters', 'PhD', np.nan, 'Bachelors', 'Masters', 'PhD',np.nan]
}

df = pd.DataFrame(data)

dropRows = df.dropna()

print(dropRows)
print(df)
