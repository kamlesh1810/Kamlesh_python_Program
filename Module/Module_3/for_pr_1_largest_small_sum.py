li=[]
num=int(input("Enter a number of list element: "))
for i in range(1,num+1):
    el=int(input("Enter element: "))
    li.append(el)
li.sort()    
print("After sort: ",li)
print("Small element is: ",li[0])
print("Largest element is: ",li[num-1])
print("After sum of all from a list")
sum=0
for i in li:
    sum=i+sum
print("Sum is: ",sum)    


