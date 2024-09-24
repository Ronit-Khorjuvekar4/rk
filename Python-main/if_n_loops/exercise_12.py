#Exercise 13: Find the factorial of a given number

n = 5
count = 0
fact = 1

for i in range(1,n + 1):
    fact *= i 
    
print(fact)