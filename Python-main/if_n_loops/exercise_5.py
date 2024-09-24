#Exercise 6: Count the total number of digits in a number

n = 75869
count = 0
newN = str(n)

while count <= len(newN) - 1:
    count += 1
    
print("Count : ",count)