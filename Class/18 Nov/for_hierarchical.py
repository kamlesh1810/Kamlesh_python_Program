import random
class A:
    def getA(self,b):
        self.a=b                        #   self.a ek nya variable bn rha h🚩   
        # print("Pass  : ",self.a)
    def putA(self):
        if self.a==x:
            print("A's value using X's : ",self.a)
        elif self.a==y:
            print("A's value using Y's  : ",self.a)    
        else:
            print("A's value usinf Z's : ",self.a)    

class B(A):
    def getB(self,b):
        self.a=b  
    def putB(self):
        print("A : ",self.a)

class C(A):
    def getC(self,b):
        self.a=b    
    def putC(self):
        print("A : ",self.a)

class D(A):
    def getD(self,b):
        self.a=b  
    def putD(self):
        print("A : ",self.a)


x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))
z=int(input("Enter a value for z : "))

obj1=B()    
obj2=C()
obj3=D()
# obj1.getA(x)
ran=random.choices(x,y,z)    #  🏮 random ka nhi ho rah h 🏮
obj2.getA(ran)
# obj3.getA(z)

# obj1.putA()
obj2.putA()
# obj3.putA()





                
