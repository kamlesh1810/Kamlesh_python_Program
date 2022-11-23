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