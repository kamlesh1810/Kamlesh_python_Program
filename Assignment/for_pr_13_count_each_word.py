#  <-- count char without loop -->

# str=input("Enter any string: ")
# print(str)
# chr=input("Which character do you want to count: ")
# print(f"Total {chr} is: ", str.count(chr))


#Question is --> Is the same code 
# Answer --> No, this code is not generate same output at all when we count perticular one word(using below program) its couldn't count

str = input("Enter any string: ")
chr = input("Enter a character to check frequency: ")
count = 0
for i in str:
    if i == chr:
        count += 1
print(chr, "occurs", count, "time(s)")
