fileName = "file_2.txt"
with open(fileName, 'r') as givenfilecontent:
    wrds = givenfilecontent.read().split()

max = len(max(wrds, key=len))

rslt = [word for word in wrds if len(word) == max]
print(*rslt)


