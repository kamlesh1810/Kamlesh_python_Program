def fun(a,b):
    return a*b


def fun(a,b,c):
    return a*b*c

# print(fun(2,3))   ehown an error bcoz python does not support overloading
print(fun(2,3,5))

# The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 