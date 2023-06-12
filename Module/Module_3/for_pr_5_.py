li1 = []
li2 = []
num1 = int(input("Enter a number for first list elements: "))
for i in range(0, num1):
    el1 = input("Enter element: ")
    li1.append(el1)

num2 = int(input("Enter a number for second list elements: "))
for i in range(0, num2):
    el1 = input("Enter element: ")
    li2.append(el1)

print("First list: ", li1)
print("Second list: ", li2)

for i in li1:
    for j in li2:
        if i == j:
            print(True)
        