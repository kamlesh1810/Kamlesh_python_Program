li=[]
for i in range(2000,3001):
    conv=str(i)
    if int(conv[0])%2==0 and int(conv[1])%2==0 and int(conv[2])%2==0 and int(conv[3])%2==0:      
        li.append(conv)
print(li)        
