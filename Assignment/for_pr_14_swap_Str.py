str1=input("Enter any name: ")
str2=input("Enter any name: ")
print("Before swapping A: ",str1,"B: ",str2)
first=str2[:2]+str1[2:]
second=str1[:2]+str2[2:]
# newStr=first+second

print("New string: ",first+" "+second)