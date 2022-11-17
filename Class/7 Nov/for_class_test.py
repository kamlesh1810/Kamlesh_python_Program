# Tast 1
# n=int(input("Enter n: "))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)


# Tast 2

# li=[]
# for i in range(1000,2000+1):
#     if i%7==0 and i%5 !=0:
#         li.append(i)
# print(li)

#   WAP a program to  print number bw 2000 and 3000 where all 4 digits should be even number and not odd

# Tast 3
# li = []
# for i in range(2000, 3001):
#     i = i%2
#     if i and i%3==0:
#         li.append(i)
# print(",".join(li))

li = []
for i in range(200, 300+1):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        li.append(s)
print(li)
