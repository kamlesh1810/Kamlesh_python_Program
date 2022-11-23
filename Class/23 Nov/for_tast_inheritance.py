class side:

    def get(self):
        self.num=num
        


class square (side):
    def funSquare(self):
        print("The Square is :", num*num)


class cube(side):
    def funCude(self):  
        print("The cube is : ",self.num*self.num*self.num)
        # print("The cube is : ",self.num**self.num)

num=int(input("Enter a Vulue : "))
obj1 = square()
obj2 = cube()
obj1.get()
obj1.funSquare()
obj2.get()
obj2.funCude()
