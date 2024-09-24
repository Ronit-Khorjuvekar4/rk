#Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i,data in enumerate(list1):
    if data == "":
        list1.pop(i)

print(list1)


# res = list(filter(None, list1))
# print(res)