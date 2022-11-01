def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


# str = input("Enter a string: ")

# snot = str.find("not")
# spoor = str.find("poor")

# if snot > snot and snot > 0 and spoo > 0:
#     str = str.replace(str[snot:(spoor+4)], "good")
#     print("After Change:  ", str)
# else:
#     print(str)
