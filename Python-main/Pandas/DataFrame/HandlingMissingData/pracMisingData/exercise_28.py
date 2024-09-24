# What method would you use to fill missing values in the ExperienceYears column based 
# on a linear regression model using Age as the predictor?
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
from sklearn.linear_model import LinearRegression

# Creating a Linear Regression model
model = LinearRegression()

# Preparing the data
train_data = df[['Age', 'ExperienceYears']].dropna()
X_train = train_data[['Age']]
y_train = train_data['ExperienceYears']

# Fitting the model
model.fit(X_train, y_train)

# Predicting missing values
missing_values = df[df['ExperienceYears'].isna()]
X_missing = missing_values[['Age']]
df.loc[df['ExperienceYears'].isna(), 'ExperienceYears'] = model.predict(X_missing)

print(df)



