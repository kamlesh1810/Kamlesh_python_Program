class Demo:
    x = 0

    def maxOfTwo(self, a, b):
        if a > b:
            print(a, " is greater")
        else:
            print(b, " is greater")

    def fibonacci(self, x):
        self.x = a
        n = 0
        f = 1
        sum = 0
        while sum < self.x:
            print(sum)
            n = f
            f = sum
            sum = n+f


obj = Demo()
num1 = int(input("Enter a value for A : "))
num2 = int(input("Enter a value for B :"))
obj.maxOfTwo(num1, num2)

a = int(input("Enter number which you want to fibonacci series : "))
obj.fibonacci(a)
