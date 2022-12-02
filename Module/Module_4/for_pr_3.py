inputFile = "firstN_Line.txt"

n = int(input("Enter N value: "))

with open(inputFile, 'r') as filedata:
    f=filedata.readlines()
    print(f"The following are the first {n} lines of a text file:")

for textline in (f[:n]):
    print(textline, end ='')
filedata.close()