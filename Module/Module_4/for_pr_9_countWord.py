from collections import Counter

file='file_2.txt'
with open(file) as f:
    count=Counter(f.read().split())
print(count)    
