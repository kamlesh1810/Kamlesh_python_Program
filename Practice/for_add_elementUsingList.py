tpl=()
num=int(input("Enter a number for tuple elemet : "))
tp=list(tpl)
for i in range(num):
    el=input("Enter an element : ")
    tp.append(el)
tpl=tuple(tp)
print(tpl)    
print(type(tpl))