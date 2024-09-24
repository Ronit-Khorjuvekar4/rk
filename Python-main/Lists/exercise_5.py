#Exercise 5: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list3 = [i for i in zip(list1,list2[::-1])]

print(list3)