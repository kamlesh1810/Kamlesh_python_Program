class A:
    def getA(Self):
        print("pass")
        # if Self==self:
        #     print("It's not sensitive ")
        # else:
        #     print("It's sensitive ")    
    def putA(self):
        pass

class B (A):
    def getB(self):
        pass
    def putB(self):
        pass

obj=B()
obj.getA()
# obj.getA('Self')


