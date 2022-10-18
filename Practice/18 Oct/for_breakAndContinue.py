num = int(input("Enter a number: "))
skipValue = 0
# chr=int(input("Which you wnat to skip value b/w given number: "))
# for i in range(1, num+1):
#     if i == chr:
#         skipValue = i
#         continue
#     print(i)
# print("Skip value is: ",skipValue)  


chr=int(input("With which number do you want to break the loop: "))
for i in range(1,num):
    if i==chr:
        print("Loop is breaked...!")  
        break
    else:
        print(i)

  