a= int(input("Enter a value for A: "))
b= int(input("Enter a value for B: "))
print("Before swapping: A = ",a,"B = ",b)
a,b=b,a
print("After swapping: A = ",a,"B = ",b)



# <-- with temp variable -->

a= int(input("Enter a value for A: "))
b= int(input("Enter a value for B: "))
print("Before swapping: A = ",a,"B = ",b)
c=a
a=b
b=c
print("After swapping: A = ",a,"B = ",b)
