import for_tast

while True:
    # print("Press 1:UDF function: ")
    print("Press 1:maxOfTwo")
    print("Press 2:maxOfThree")
    print("Press 3:evenOdd")
    print("Press 4:prime number")
    print("Press 5:Fibonaci series")
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter a value: "))
        b = int(input("Enter a value: "))
        for_tast.maxOfTwo(a, b)

    elif choice == 2:
        a = int(input("Enter a value: "))
        b = int(input("Enter a value: "))
        c = int(input("Enter a value: "))

        for_tast.maxOfThree(a, b, c)
    elif choice == 3:
        a = int(input("Enter a value for a: "))
        for_tast.evenOdd(a)

    elif choice == 4:
        num = int(input("Enter the input Range : "))
        for_tast.primeNum(num)

    else:
        num=int(input("Enter a value: "))    
        for_tast.fib(num)
        break
    print()