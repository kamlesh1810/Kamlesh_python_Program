l = [('A', 'B', 'C'), (1, 2, 3), ('a', 'b', 'c')]
print([t[:-1] + (100,) for t in l])


# for i in range(5):
#     print(" "*(5-i)," *"*i)
# for i in range(5,0,-1):
#     print(" "*(5-i)," *"*i)


for i in range(1,5+1):
    print("* "*i)