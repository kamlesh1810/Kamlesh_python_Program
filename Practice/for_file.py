# file=open("file.txt",'w')
# file.write("Hello this is kamlesh suthar... :)")
# file.close()

# print("For read oparetion")
# file=open("file.txt",'r')
# print(file.read())
# file.close()


# print("For appending: ")
# file=open("file.txt",'a')
# file.write(" from Rajasthan")
# file.close()


# file=open("file.txt",'w+')
# file.write("How are you?")
# print(file.tell())
# print(file.read())
# file.close()


f = open("file.txt")
content = f.read(6)
print("1 ", content)

cont = f.read()
print("2: ", cont)
f.close()
