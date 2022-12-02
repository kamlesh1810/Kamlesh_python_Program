from collections import Counter

file='countWord.txt'
with open(file) as f:
    count=Counter(f.read().split())
print(count)    
