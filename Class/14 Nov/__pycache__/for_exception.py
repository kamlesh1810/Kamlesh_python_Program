while True:
    try:
        n=float(input("Enter a value: "))
        n1=int(n)
    except Exception:
        print("Invailid input")    
    finally:
        print("Finally called")  
          
print("Bye")        
