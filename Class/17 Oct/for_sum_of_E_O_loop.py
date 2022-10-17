num = int(input("Enter a number: "))

eSum = 0
oSum =0
for i in range(1,num+1):
    if i%2==0:
        eSum = eSum+i
    else:
        oSum = oSum+i    
       
print("Number of Even sum: ",eSum) 
print("Number of Odd sum: ",oSum)