#Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]


size = len(list1) - 1
print(size)
for i in range(size, -1, -1):
    print(list1[i])