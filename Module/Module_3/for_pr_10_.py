li=[]
num = int(input("Enter a number of list element: "))
for i in range(0,num):
    el=int(input("Enter elememt: "))
    li.append(el)

min=li[0]
for i in range(num):
    if min>li[i]:
        min=li[i]

sMin=li[0]
for i in range(num):
    if sMin>li[i]:
        if li[i]!=min:
            sMin=li[i]

print("\nsecond smallest number is")            
print(sMin)
        


