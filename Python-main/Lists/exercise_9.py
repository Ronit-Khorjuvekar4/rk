#Exercise 9: Replace list’s item with new value if found
#You have given a Python list. 
# Write a program to find value 20 in the list, and if it is present, 
# replace it with 200. Only update the first occurrence of an item.
#[5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]
list2 = list(list1)
print(list2)
count = 0

for i,data in enumerate(list1):
    if count == 0:
        if data == 20:
            count += 1
            list1.pop(i)
            list1.insert(i,200)

print(list1)