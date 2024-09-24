# Exercise 2: Create a function with variable length of arguments

def func1(*args):
    for i in args:
        print(i)

func1(2,3,4)
func1(10,11,12,13)