keys = []
values = []
n = int(input("Enter number of elements for dictionary : "))
print("For keys : ")
for x in range(0, n):
    element = int(input("Enter element" + str(x+1) + " : "))
    keys.append(element)
print("For values : ")
for x in range(0, n):
    element = int(input("Enter element" + str(x+1) + " : "))
    values.append(element)
d = dict(zip(keys, values))
# mList=list(zip(*li))
print("The dictionary is : ")
print(d)

#    1. Declare two empty lists and initialize them to an empty list.
#    3. Consider a for loop to accept values for the two lists.
#    4. Take the number of elements in the list and store it in a variable.
#    5. Accept the values into the list using another for loop and insert into the list.
#    6. Repeat 4 and 5 for the values list also.
#    7. Zip the two lists and use dict() to convert it into a dictionary.
#    8. Print the dictionary.
#    9. Exit.
