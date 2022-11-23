'''
Inheritance: - It is creating  a new class from an already existing class

Note--> Obj will always be created of derived/child class


Type of inheritance: 
    1) Single-level inheritance
    2) Multi-level inheritance
    3) Hierarchical  inheritance
    4) Multiple inheritance
    5) Hybrid inheritance


'''


class A:
    def getData(self,a):
        self.a=a

    def putData(self):
        print("A : ",self.a)    


class B(A):
    def getB(self, b):
        self.b=b       

    def putB(self):
        print("B : ",self.b)    

a=int(input("Enter a value : "))
b=int(input("Enter a value : "))

obj=B()
obj.getData(a)
obj.getB(b)
obj.putData()
obj.putB()




