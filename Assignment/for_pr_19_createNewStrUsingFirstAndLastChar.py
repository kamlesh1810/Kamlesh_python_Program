str = input("Enter any string: ")
if len(str) <= 2:
    print("The given string len less then2")
else:
    print("New string is: ",str[0:2]+str[-2:])


