d={1:"Ram",2:"Vikash",3:"Chinky",4:"Purvesh",5:"Anu",6:"Anu"}
print("Original dictionary: ",d)
# print()
# print(d[4])
# d1=d.copy()

# print("D1: ",d1)

# print(d1.get(1))
# print(d.items())
# print(d.values())
# print(d.keys())

# print(d.pop(5))  # It remove only last value
# print(d)

# print(d.popitem())  #It remove last item with key and value
# print(d)


d2={5:"Kiran, Kalpesh"}
d.update(d2)
print(d)



d[5]="Kamal"
print(d)

for i in d:
    print(i,":",d[i])

