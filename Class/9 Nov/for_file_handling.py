
file=open("file_handling.txt",'w')
file.write("This is file management using python ")
file.close()
print("File created successfully")

print("Read ")
file=open("file_handling.txt",'r')
print(file.read())
file.close()



print()
print("Append operation")

file=open("file_handling.txt",'a')
file.write('Now hear this is data')
file.close()

print("Data appended successfully")

