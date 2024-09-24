#Exercise 10: Remove all occurrences of a specific item from a list.
#Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]


for i,data in enumerate(list1):
    if data == 20:
        list1.pop(i)

print(list1)