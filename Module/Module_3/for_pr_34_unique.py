dict = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita','545':'Siya'}
li =[] 
print("Dictionary with duplicate value : ",dict)
for i in dict.values(): 
  if i in li: 
    continue 
  else:
    li.append(i)
print(li)    










