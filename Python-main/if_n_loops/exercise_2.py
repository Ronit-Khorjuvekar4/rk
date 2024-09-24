#Exercise 3: Calculate the sum of all numbers from 1 to a given number

num = 10
sum = 0

for i in range(1,num+1):
    sum += i
    i += 1

print("Sum : ", sum)