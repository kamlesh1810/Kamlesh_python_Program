# a= input("Enter you first name:")
# b= input("Enter you last name:")
# print("Hello",a,"",b)  #concat string
# print(a,"",b)

li=[]
for i in range(1000,2000+1):
    if i%7==0 and i%5 !=0:
        li.append(i)
print(li)
