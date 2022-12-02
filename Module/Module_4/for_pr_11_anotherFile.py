f1=open('file1.txt','r')
f2=open('file2.txt','r')

print("Content of first file before appending : ",f1.read())
print("Content of second file before appending :\n",f2.read())


f1.close()
f2.close()


f1=open('file1.txt','a+')
f2=open('file2.txt','r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Content of first file after appending : ",f1.read())
print("Content of second file after appending : ",f2.read())


