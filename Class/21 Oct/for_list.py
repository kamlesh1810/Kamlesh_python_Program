# # l=[1,2,44.4,23,"Apple","Pear",False,True,"Banana"]
# # print("List: ",l)

# # l.append("pineapple")
# # print()
# # print("After append some value in list: ",l)
# # print()
# # sb_l=l.count("Apple")
# # print(sb_l)

# # print(l.sort())
# # # l.insert(8,bool) #also right (o/p--> <clas 'bool'>)
# # # print(l)


# li = [5, 6, 8, 5, [5, 65], 6, 5]
# li.sort()
# print(li)
# # print("Length of li list: ", len(li))


from asyncio.windows_events import NULL
from cgi import print_arguments
from contextlib import nullcontext


li=[454,56,988,1,25,11,7,18,]
li.sort()
print(li)           # by default --> ascending 

li2=[101,201,301]
print(li2)
print()
li.extend(li2)
print("After extend the list li2 in li: ",li)
if li.clear():
    print("list is empty")
else:
    print("List is not empty")    
# print(li)

# li.remove()