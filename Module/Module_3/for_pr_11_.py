li = []
num = int(input("Enter a number for list: "))
for i in range(0, num):
    el = input("Enter element: ")
    li.append(el)

new = []

for i in li:
    if i not in new:
        new.append(i)

print("Unique element from this list : ",new)







      
