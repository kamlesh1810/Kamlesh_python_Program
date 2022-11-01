str = input("Enter any string: ")
chr = input("Enter a character to check frequency: ")
count = 0
for i in str:
    if i == chr:
        count += 1
print(chr, "occurs", count, "time(s)")