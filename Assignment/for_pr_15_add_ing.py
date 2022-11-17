str = input("Enter a string: ")
if len(str)>2:
    if str.endswith("ing"):
        print(str+'ly')
    else:    
        print(str+"ing")
else:
    print("The length of given string is lessthen 2 plz enter a another string...!")        





