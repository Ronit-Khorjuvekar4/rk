# Exercise 2: Remove and add item in a list

# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list1 = [34, 54, 67, 89, 43, 94]

print("Original list:", list1)


list1.pop(4)
print("\nList after removing value from index 4:", list1)
list1.insert(2,15)
print("List after adding value at index 2:", list1)


