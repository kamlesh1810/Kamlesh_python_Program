dict = {1:'Raju', 2: 'Laxman', 3: 'Ram', 4: 'Raj', 5: 'Seth', 6: 'Shyam'}
print(dict)
i=int(input("Enter key which you want to check : "))
if i in dict:
    print("Key is present in this dictionary")
    print("Value =",dict[i])
else:
    print("Kye is not present in this dictionary...")    




