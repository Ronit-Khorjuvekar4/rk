# Exercise 4: Write a program to print multiplication table of a given number

num = 2
multiply = 0

for i in range(1,11):
    multiply = num * i
    print(f"\nMultiplication table of {num}*{i} : ", multiply)