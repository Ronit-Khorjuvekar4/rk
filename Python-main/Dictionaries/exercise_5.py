#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

new = dict()

keys = ["name", "salary"]

for i in keys:
    new.update({i:sample_dict[i]})

print(new)