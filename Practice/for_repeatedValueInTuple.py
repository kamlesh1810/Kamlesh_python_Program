# tpl=(1,5,5,4,1,2,3,'dear',True,False)
# print(tpl)
# c=input("Enter a character your you want to count: ")
# print(tpl.count(5))


tup=(1,3,4,32,1,1,1,32)  
for i in tup:
    if tup.count(i) > 1:
        print('REPEATED',i)
        
