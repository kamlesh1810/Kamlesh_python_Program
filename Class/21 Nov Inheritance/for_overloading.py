'''
TO print object def __str__ () is used

'''


class A:
    def __init__(self,x,y) -> None:
        print("init called")
        self.x=x
        self.y=y
    
    def __str__(self) -> str:
        print("str called")    

        return "[{0}, {1}]".format(self.x,self.y)

    def __add__(self,i):
        x=self.x+i.x
        y=self.y+i.y
        return (x,y)      
        # print("Addition function called")

obj1=A(1,2)
print(obj1) 
obj2=A(3,4)
print(obj2)

print("Addition : ",obj1+obj2)
