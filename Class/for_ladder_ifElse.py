name = input("Enter a name")
maths= int(input("Enter a number for maths : "))
Phy= int(input("Enter a number for Physics. :"))
chem= int(input("Enter a number for chem. :"))


total = maths+Phy+chem
per = total/3


print("Total is :",total)
print("Per. is :",per)

if per>=80:
    print("Distinction")
elif per>=70:
    print("First division")    
elif per>=60:
    print("Second div.")
elif per>=40:
    print("pass")

else:
    print("Fail......!")    
