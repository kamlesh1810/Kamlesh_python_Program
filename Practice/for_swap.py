a=int(input("A:"))
b=int(input("B:"))

print("Before swapping")
print("A:",a,"B:",b)
a=a+b
b=a-b
a=a-b
# a,b=b,a
print("After swapping")
print("A:",a,"B:",b)
