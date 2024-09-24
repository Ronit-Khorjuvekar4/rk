# Exercise 5: Create an inner function to calculate the addition in the following way

def outer(a, b):
    square = a ** 2

    def inner(a, b):
        return a + b
    
    add = inner(a, b)
    return add + 5

result = outer(5, 10)
print(result)
