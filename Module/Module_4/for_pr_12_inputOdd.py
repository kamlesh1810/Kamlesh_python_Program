num = int(input("Enter a number: "))

try:
    if num%2!=0:
        print("Entered number is odd",num)
except :
    print("Plz enter only odd number") 
else:
    pass        
finally:
    print("Finally clause executed")




