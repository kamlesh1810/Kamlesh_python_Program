import sys

num = int(input("Enter a number: "))

try:
    if num%2!=0:
        print("Entered number is odd",num)
except Exception as e:
    print("Plz enter only odd number",e.__class__) 
else:
    pass        
finally:
    print("Finally clause executed")




