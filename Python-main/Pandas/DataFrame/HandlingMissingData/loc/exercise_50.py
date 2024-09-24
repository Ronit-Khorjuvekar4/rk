# Use loc to fill missing values in the Age column 
# with the median age of employees whose Salary is greater than 60000.
#
import pandas as pd
import numpy as np

# Creating a sample dataset with missing values and various data types
data = {
    'EmployeeID': range(101, 131),
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eva', 'Frank', np.nan, 'Hannah', 'Ian', 'Jane', 'Kyle', 'Laura', 'Mona', 'Nate', 'Olivia', np.nan, 'Quinn', 'Ray', np.nan, 'Sophia', 'Tom', 'Uma', 'Victor', 'Wendy', np.nan, 'Yvonne', 'Zack', 'Amber', np.nan, 'Blake'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', np.nan, 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', np.nan, 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance', np.nan, 'HR', 'IT', 'Finance', 'IT', np.nan, 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, np.nan, 70000, 52000, np.nan, 62000, 50000, 61000, 70000, 58000, 64000, 72000, 52000, np.nan, 66000, 63000, 54000, 71000, 69000, 60000, np.nan, 57000, 65000, 55000, 68000, np.nan, 62000, 64000, 70000],
    'JoiningYear': [2015, 2016, 2017, 2018, np.nan, 2020, 2017, 2015, 2018, 2016, 2019, np.nan, 2017, 2018, 2016, 2020, 2019, 2015, np.nan, 2018, 2017, 2016, 2015, 2020, 2019, 2018, np.nan, 2015, 2020, 2019],
    'Age': [25, 28, 30, 35, 22, np.nan, 26, 29, np.nan, 27, 24, 33, 31, np.nan, 26, 40, 28, 34, 32, 29, np.nan, 37, 22, 30, 25, 35, 28, 33, np.nan, 26],
    'ExperienceYears': [5, np.nan, 3, 7, 1, 15, 2, 6, 10, 4, 8, np.nan, 9, 7, np.nan, 5, 12, np.nan, 8, 6, 14, 4, np.nan, 11, 10, 9, np.nan, 6, 5, 13],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', np.nan, 'F', 'M', 'F', 'M', 'F', np.nan, 'M', 'F', 'M', 'F', 'M', 'M', 'F', np.nan, 'F', 'M', 'F', 'M', np.nan, 'F', 'M', 'F', 'M'],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', np.nan, 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas', 'New York', np.nan, 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', np.nan, 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas', 'New York'],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', 'Masters', 'PhD', np.nan, 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'PhD', 'Bachelors', 'Masters', 'PhD', np.nan, 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'Bachelors', 'PhD', 'Masters', 'PhD', np.nan, 'Bachelors', 'Masters', 'Bachelors', 'PhD']
}

df = pd.DataFrame(data)

median_age = df.loc[df['Salary'] > 60000, 'Age'].median()
df.loc[df['Age'].isna(), 'Age'] = median_age

print(df)

