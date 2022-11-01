str = input("Enter any string: ")
print(str)
if len(str) < 2:
    print("The given string len less then2")    
else:
    print(str[0:2]+str[-2:])    
