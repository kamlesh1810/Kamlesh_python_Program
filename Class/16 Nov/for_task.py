class demo:
    x = 0
    y = 0
    z = 0

    def __init__(self,x,y,z) -> None:
        self.x = n1
        self.y = n2
        self.z = n3

    # def __init__(self,x,y,z) -> None:
    #     self.x = n1
    #     self.y = n2
    #     self.z = n3
        

    def show(self):
        if self.x > self.y:
            if self.x > self.z:
                print(self.x, " is greater")
            else:
                print(self.z, " is graeter")
        elif self.y > self.z:
            print(self.y, " is greater")
        else:
            print(self.z, " is greater")

    def fib(self):
        # self.x = fi
        fi = int(input("Enter a number for fibonacci series: "))
        n = 0
        f = 1
        sum = 0
        while sum < fi:
            print("With loop    ",sum)
            n = f 
            f = sum
            sum = n+f
          
        print(sum)    


n1 = int(input("Enter a value: "))
n2 = int(input("Enter a value: "))
n3 = int(input("Enter a value: "))
obj = demo(n1, n2, n3)
obj = demo()
obj.show()

obj.fib()
