#  0 1 2  3   4   5   6     7       8       9    0    1   2    3     4    -->Positive index number
# t=(1,2,3,1.1,2.2,3.3,True,'tops',[10,20,30],10,False,1.1,2.2,True,'python')
#  5 4 3  2   1   0    9     8        7      6   5    4   3    2     1      -->Negative index number


# print(t[-10:-6])
# print(t)
# print(t[1:9])
# print(t[:7])
# print(t[13:])
# print(t[2:5:2])
# print(t[::4])
# print()
# print()
# print(t[-4:-12])
# print(t[:-6])
# print(t[-4:])
# print(t[-3:-12:-2])
# print(t[::-1])


# def add(a,b):
#     print(a/b)
    


# def mut(func):
#     def inner(a,b):
#         return add(a*b)
#     return inner    
# obj =mut(add)
# obj(4,2)






# def dec(func):
#     def inner(a,b):
#         print(a*b)
#         func(a,b)
#         print(a-b)     # line 42 and 43 dec function ki lines h
#     return inner    

# def name(a,b):
#     print(a+b)    

# name=dec(name)    
# name(4,2)



# To take input from the user
#num = int(input("Enter a number: "))
# num=int(input("Enter a number : "))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#         #    print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")




a=5
for i in range(a+1):
    print(" "*(a-i)," *"*i)
for i in range(a-1,0,-1):    
    print(" "*(a-i)," *"*i)
    