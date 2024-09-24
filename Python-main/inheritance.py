class A:
    a = 0
    b = 0
    ans = 0

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        print("A :",self.a)
        print("B :",self.b)
        print("Answer :",self.ans)

    def calculate(self):
        self.ans = self.a + self.b

class B(A):

    def __init__(self,a,b):
        super().__init__(a,b)

obj = B(10,20)
obj.calculate()
obj.display()