#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for index,item in enumerate(l1):
    if(index % 2 != 0):
        l3.append(item)
        
for index,item in enumerate(l2):
    if(index % 2 == 0):
        l3.append(item)

print(l3)