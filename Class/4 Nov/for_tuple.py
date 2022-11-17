from traceback import print_tb


t=('a','b','c','d','a',6,3,2,5,[],2,2.3,True,False)
print(t)
print(t.count(1))
print(t.index([]))

t[9].append(5)
t[9].append(33)
t[9].append('xyz')
t[9].append('abc')
print(t[9])

# for i in t:
#     print(i)
# print(6 in t)



