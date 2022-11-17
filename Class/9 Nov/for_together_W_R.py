file=open("file_handling.txt",'w+')
file.write("This is read/write operation in python using w+")
print("File pointer current position: ",file.tell())
file.seek(25)
print(file.read())
file.close() 

