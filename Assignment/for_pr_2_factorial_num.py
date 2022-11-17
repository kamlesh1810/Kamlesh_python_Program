n = int(input("Enter a number: "))
fact = 1
if n<0:
    print("Factorial no. cann't be negative number..")
else:
    while n > 1:
        fact = fact*n
        n = n-1
    print("The factorial of given number: ",fact)    
    