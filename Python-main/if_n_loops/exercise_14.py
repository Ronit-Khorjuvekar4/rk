# Exercise 15: Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
count = 1
for i in my_list:
    if(count % 2 == 0):
        print(i)
    count += 1