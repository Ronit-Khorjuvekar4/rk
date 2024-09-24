#Exercise 2: Print the following pattern

i = 1
n = 5

for i in range(1,n+2,1):    
    for j in range(1,i):
        print(j,end=' ')
    print("")
    i+=1
