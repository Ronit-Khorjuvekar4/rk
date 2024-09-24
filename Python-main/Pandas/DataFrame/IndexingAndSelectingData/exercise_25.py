# Filter the DataFrame to show only employees whose Age is either the maximum or the minimum in the DataFrame.
import pandas as pd

data = {
    'employeeid': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 55000, 70000, 52000],
    'joiningYear': [2015, 2016, 2017, 2018, 2019],
    'age': [25, 28, 30, 35, 22]
}

df = pd.DataFrame(data)

age_max_or_min = df[(df['age'] == df['age'].max()) | (df['age'] == df['age'].min())]
print(age_max_or_min)
