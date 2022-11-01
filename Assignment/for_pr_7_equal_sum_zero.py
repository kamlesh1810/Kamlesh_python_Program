a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c = int(input("Enter value for c:"))

if a == b:
    sum = 0
    print("Equal value so sum will be zero")
elif a == c:
    sum = 0
    print("Equal value so sum will be zero")
elif b == c:
    sum = 0
    print("Equal value so sum will be zero")
else:
    sum = a+b+c
    print("Sum: ", sum)
