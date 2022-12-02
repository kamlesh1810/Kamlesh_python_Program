file='file_2.txt'
with open(file) as f:
    line=f.readlines()
    totalLine=0
    for i in line:
        totalLine=totalLine+1
    print(totalLine)    