# dict1 = {1: 15, 2: 8, 3: 6}
# dict2 = {4: 16, 3: 12, 6: 10}
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}
print("First dictionary : ",d1)
print("Second dictionary : ",d2)

for i in d2:
   if i in d1:
      d2[i] = d2[i] + d1[i]
   else:
      pass
result = d1|d2
print(result)
