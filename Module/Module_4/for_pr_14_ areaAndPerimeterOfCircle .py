class Circle:
    def __init__(self,r) -> None:
        self.radius=r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*3.14*self.radius
        

num=int(input("Enter a area and perimeter of Circle : "))

obj=Circle(num)

print(f"The area  of Circle  : ",obj.area())
print("The perimeter of Circle : ",obj.perimeter())



