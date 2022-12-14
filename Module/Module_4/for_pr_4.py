inputFile = "firstN_Line.txt"
n = int(input("Enter N value: "))

with open(inputFile, 'r') as filedata:
    f=filedata.readlines()
    print(f"The following are the last {n} lines of a text file:")

for i in (f[-n:]):
    print(i, end ='')
filedata.close()