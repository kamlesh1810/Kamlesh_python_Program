'''
num=int(input("Enter a number for factorial : "))
result=1
while num>=1:
    result=num*result
    num=num-1
print(result)

'''

'''
num = int(input("Enter a number : "))
n = 0
sum = 0
f = 1

while(sum<=num):
    print(sum)
    sum = f+n
    n=f
    f=sum
'''
    


'''
--> pyramid

for i in range(1,9+1):
    print(" "*(9-i)," *"*(i))
'''


t=(1,2,5,2,5,2,5,2,5,5)
print(t)
s={11,5,2,6,6,2,1,5,2,1,5}
print(s)


'''
str='Kamlesh'
print(str[::-1])
result =""
for i in str:
    result=i+result
print(result)

result =""
result="".join(reversed(str))
print("Reversed string : "+result )

'''
