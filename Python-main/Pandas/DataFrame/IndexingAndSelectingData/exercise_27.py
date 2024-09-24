# Retrieve the Department and JoiningYear of employees whose Name starts with a vowel and ends with a consonant.
import pandas as pd

data = {
    'employeeid': [101, 102, 103, 104, 105,106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','ejh'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR','HR'],
    'salary': [50000, 60000, 55000, 70000, 52000,42000],
    'joiningYear': [2015, 2016, 2017, 2018, 2019,2020],
    'age': [25, 28, 30, 35, 22,24]
}

df = pd.DataFrame(data)

vowel_consonant_names = df[df['name'].str.match(r'^[AEIOUaeiou].*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$')][['department', 'joiningYear']]
print(vowel_consonant_names)
