# str="Hello this is  kamlesh form Raj"
# # print(len(str))
# print(str)
# addStr=input("Add some string in middle of this string: ")
# start_str=str[:15]
# end_str=str[15:]
# print("After add string: ",start_str+addStr+end_str)

fStr=input("Enter any string: ")
# Printing original string
print("The original string is: ",str(fStr))

# Initializing mid string 
mStr=input("Enter string to insert in middle: ")

# spliting string in list
temp =fStr.split()
print(temp)
mPos=len(temp)

# Appending in mid
result=temp[:mPos]+[mStr]+temp[mPos:]


# conversion back
result=" ".join(result)

# printing result
print("Formulated string: "+str(result))

