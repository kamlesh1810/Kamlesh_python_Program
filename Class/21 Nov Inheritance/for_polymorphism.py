class A:
    def show(self):         #--> self keyword nhi h, use
        print("Show from A ")
class B(A):        
    def show(self):
        super().show()
        print("Show from B")
class C(B):
    def show(self):
        print("Show from C")        

obj=C()        
obj.show()

