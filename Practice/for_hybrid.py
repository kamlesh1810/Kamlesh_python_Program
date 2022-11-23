class A:
    def fun_A(self):
        print("This is from Class A")

class B(A):
    def fun_B(self):
        print("This is from Class B")        

class C(A):
    def fun_C():
        print("This is from Class C")

class D(B,C):
    def fun_D():
        print("This is from Class D")


obj=D()
obj.fun_A()
obj.fun_B()
obj.fun_C()
obj.fun_D()
