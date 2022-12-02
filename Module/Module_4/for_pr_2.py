f=open("file.txt",'r')
print("Before Appanding file's content : ",f.read())
f.close()

f=open("file.txt",'a')
f.write(" Form Rajasthan")

f.close()


f=open("file.txt",'r')
print(f.read())

f.close()