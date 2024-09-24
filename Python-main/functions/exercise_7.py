# Exercise 7: Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

showStudent = display_student
showStudent("Emma", 26)
