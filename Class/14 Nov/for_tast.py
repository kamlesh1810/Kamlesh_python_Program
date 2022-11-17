def maxOfTwo(a, b):
    if a > b:
        print("A is greater")
    else:
        print("B is greater")


def maxOfThree(a, b, c):
    if a > c:
        if a > b:
            print("A is greater")
        else:
            print("B is greater")
    else:
        if b > c:
            print("B is greater")
        else:
            print("C is greater")


def evenOdd(a):
    if a % 2 == 0:
        print(a, " is even")
    else:
        print(a, " is odd")


def primeNum(num):
    
    for iter in range(2, num):
        for i in range(2, iter):
            if (iter % i == 0):
                break
        else:
            print(iter)


def fib(num):
    n = 0
    f = 1
    sum = 0
    if num < 0:
        print("Plz enter a valid number...")
    else:
        while num >= 0:
            sum = n+f
            n = f
            f = sum
            num += 1


print()
