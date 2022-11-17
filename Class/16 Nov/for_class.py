'''
OOP --> Object oriented programming 
1) Encapsulation  2)Inheritance  3) Polymorphism  4) DAta Abstraction

'''


class demo:
    x = 0

    def __init__(self, x):
        self.x = num
        # print("This is Constructor")

    def showData(self):
        print("Entered number is: ", self.x)

    def evenOdd(self):
        if self.x % 2 == 0:
            print("Entered number is even")
        else:
            print("Entered number is odd")


num = int(input("Enter a number: "))
obj = demo(num)
obj.showData()
obj.evenOdd()
