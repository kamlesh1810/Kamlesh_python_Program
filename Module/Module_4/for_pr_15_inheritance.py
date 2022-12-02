"""
Inheritance :  Inheritance in Python Let’s better understand the concept of Python inheritance through an example.  Let’s say there exists a class “Fruit”, and you derive from it to create a new class called “Apple”. The simple relationship between the two classes says that “Apple” is a “Fruit”.    

The “Apple” class inherits the interface and implementation of the base class “Fruit”, such that Apple objects can replace Fruit objects without changing any of the desired properties in an application. This concept of substitution is called the Liskov substitution principle.


--> In Inheritance object will always be created of derived class
class fruit:
    pass

class apple(fruit):
    pass

obj=apple()

Type of Inheritance:
1) Single Inheritance :-In this type, a derived class inherits from only one base class.
2) Multiple Inheritance :-  In this inheritance, the derived class inherits from multiple base classes.
3) Multi-level Inheritance :- In this, a derived class inherits another derived class.
4) Hierarchical Inheritance :-  In this, we create more than one derived classes from one base class.
5) Hyvbrid  Inheritance :- It is the combination of multi-level and hierarchical Inheritance
    
"""



class A:
    def getA(self,a):
        self.i=a
    def putA(self):
        print("A : ",self.i)
class B:
    def getB(self,b):
        self.j=b
    def putB(self):
        print("B : ",self.j)

class C(A,B):
    def getC(self,c):
        self.k=c
    def putC(self):
        print("C : ",self.k)

x=int(input("Enter a value  : "))
y=int(input("Enter a value  : "))
z=int(input("Enter a value  : "))

obj=C()
obj.getA(x)
obj.getB(y)
obj.getC(z)

obj.putA()
obj.putB()
obj.putC()

