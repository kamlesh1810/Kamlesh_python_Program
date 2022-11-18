li = []
n = int(input("Enter number for list: "))
for i in range(0, n):
    el = input("Enter element: ")
    li.append(el)
print("Find longest element in this list: ", li)
max = len(li[0])
temp = li[0]
for i in li:
    if len(i) > max:
        max = len(i)
        temp = i
print("The word with the longest length is: ", temp)
