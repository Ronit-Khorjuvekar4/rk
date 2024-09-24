# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_list = list()

for i in speed.values():
    if i not in speed_list:
        speed_list.append(i)

print(speed_list)