'''
randoom
conditions, loop
list
'''
import random

print("Welcome to linear houste")

main_li=[]
p1=[]
p2=[]

while len(main_li)<12:
    tickect=random.randint(1,20)
    if tickect not in main_li:
        main_li.append(tickect)
print(len(main_li))        
print(main_li)

for i in main_li:
    print(i ,end='  ')
print()


random.shuffle(main_li)  #shuffle list me se random number leta h
# enter click event ke liye sirdf input likhte h

p1=main_li[:6]
p2=main_li[6:]
print(p1)
print(p2)




