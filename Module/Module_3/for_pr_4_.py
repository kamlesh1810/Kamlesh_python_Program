li=[]
num=int(input("Enter a number for list element: "))
for i in range(0, num):
    el=input("Enter element: ")
    li.append(el)
if len(li)==0:
    print("List is empty")
else:
    print("List is not empty")    