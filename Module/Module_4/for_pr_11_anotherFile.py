file1=input("Enter the name of first file : ")
file2=input("Enter the name of second file : ")


f1=open(file1,'r')
f2=open(file2,'r')

print("Content of first file before appending : ",f1.read())
print("Content of second file before appending : ",f2.read())


f1.close()
f2.close()


f1=open(file1,'a+')
f2=open(file2,'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Content of first file after appending : ",f1.read())
print("Content of second file after appending : ",f2.read())


