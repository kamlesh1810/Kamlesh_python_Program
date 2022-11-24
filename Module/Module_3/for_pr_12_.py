li=[2,3,5,8,6,8]
s_li=[8,6]

# print(li.index(3))
# print(li[1:3])
result=False

for i in range(len(li)-1):
    if li[i:i+len(s_li)]==s_li:
        result = True
        break

print("Is sublist present in list ? : "+str(result))