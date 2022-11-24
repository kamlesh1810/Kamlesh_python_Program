li=[('Hello',1),('world',2),('This',3),('is Kamlesh',4)]
print("Original list is : ")
print(li)

mList=list(zip(*li))
print("Modified list is : "+str(mList))
