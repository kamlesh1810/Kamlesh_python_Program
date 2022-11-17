str=input("Enter any string: ")
print(str)
print("Total length of this string: ",len(str))
addStr=input("Add some string in middle of this string: ")
li= str.split()  # splits a string into a list
mPos=len(li)//2  
result=li[:mPos]+[addStr]+li[mPos:]
result=" ".join(result)
print("After add string: ",result)


