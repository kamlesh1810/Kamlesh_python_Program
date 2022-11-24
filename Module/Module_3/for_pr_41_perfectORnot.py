def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        print("The entered number is a perfect number") 
         
    else:
        print("The entered number is not a perfect number")

num=int(input("Enter a number : "))    
perfect_number(num)

