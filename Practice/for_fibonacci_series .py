num = int(input("Enter number which you want to fibonacci series: "))
n=0
f=1
sum=0
while num>=0:
    sum=n+f
    n=f
    f=sum
    num =num-1
    print(sum)


