# str="Hello dear :)"
# print("Reverse string: ",str[::-1])

# str=input("Enter any string: ")
# print(str)
# result=""
# if len(str)>=4:
#     for i in str:
#         result=i+result
# else:
#     print("Length of given string is lessthen 4")        
# print(result)



def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1
print(reverse_string('abcd'))
# print(reverse_string('pyth'))