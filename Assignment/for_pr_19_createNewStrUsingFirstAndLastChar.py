str = input("Enter any string: ")
if len(str) <= 2:
    print("The given string len less then2")
else:
    print("New string is: ",str[0:2]+str[-2:])


# str = input("Enter any string: ")
# count = 0

# if len(str) >= 2:
#     for i in str:
#         count = count+1
#     new = str[:2]+str[count-2:count]
#     print("Newly formed string is ")
#     print(new)
