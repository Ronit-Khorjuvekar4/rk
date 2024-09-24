# Exercise 17: Find the sum of the series upto n terms

n = 5
temp = 2
count = 0

# run loop n times
for i in range(0, n):
    print(temp, end="+")
    count += temp
    temp = temp * 10 + 2
    print("\nafter:",temp)
print("\nSum of above series is:", count)
