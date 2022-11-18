num = int(input("Enter number which you want to fibonacci series: "))
n = 0
f = 1
sum = 0
if num < 0:
    print("plz enter a valid number...")
else:
    while sum <= num:
        print(sum)
        n = f
        f = sum
        sum = f+n
