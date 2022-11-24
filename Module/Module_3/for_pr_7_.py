li = []
num = int(input("Enter a number of list element: "))
for i in range(0, num):
    el = input("Enter element: ")
    li.append(el)
print("list: ", li)
new = []

for i in li:
    if i not in new:
        new.append(i)
print("New list with unique elements of the first list: ",new)        

