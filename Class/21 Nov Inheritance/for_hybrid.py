class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)       

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)            

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C : ",self.c)    

class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)
w=int(input("Enter a numbre : "))
x=int(input("Enter a numbre : "))
y=int(input("Enter a numbre : "))
z=int(input("Enter a numbre : "))

obj=D()        

obj.getA(x)
obj.getB(w)
obj.getC(y)
obj.getD(z)

obj.putA()
obj.putB()
obj.putC()
obj.putD()