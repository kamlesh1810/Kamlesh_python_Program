import random

''' random item from a list or tuple? '''

# tuple = (1, 2, 3, 5, "Hello", 5, "world")
# print(tuple)

# ranItem = random.choice(tuple)
# print("The generated random item form the tuple : ", ranItem)




#   Another program
# num1=random.randint(1,10)
# print("Using randint : ",num1)

# for i in range(5):
#     num2=random.randrange(10,20,3)
#     print("Using randrange : ",num2)


#   Another program


# list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# print ("Original list : ",  list)
# random.shuffle(list) #shuffle method
# print ("List after first shuffle  : ",  list)




#   Another program

random.seed(2)
print(random.random())
random.seed(3)
print(random.random())

random.seed(5)
print(random.random())

random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
random.seed(5)
print((random.random()))