class Rectangle:

    def __init__(self, w, l):
        self.width = w
        self.length = l

    def areaFun(self):
        return self.width*self.length


length = int(input("Enter a length of ractangle: "))
widht = int(input("Enter a width of rectagle: "))

obj = Rectangle(length, widht)
print("The area of Rectangle is : ", obj.areaFun())
