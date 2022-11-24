def factt(n):
    if n == 0:
        return 1
    else:
        # return n * fact(n-1)
        fact=1
        while n > 1:
            fact = fact*n
            n = n-1
        return fact    
    # print("The factorial of given number: ",fact)  
num=int(input("Input a number to compute the factiorial : "))
print(factt(num))
