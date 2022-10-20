# str="Hello this is  kamlesh form Raj"
# # print(len(str))
# print(str)
# addStr=input("Add some string in middle of this string: ")
# start_str=str[:15]
# end_str=str[15:]
# print("After add string: ",start_str+addStr+end_str)


def not_poor(str1):  
  snot = str1.find('not')  
  sbad = str1.find('poor')  
  
  if sbad > snot:  
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')  
  
  return str1  
print(not_poor('The lyrics is not that poor!'))  











