from collections import deque

l = deque([])
l.append(1)
l.append(1)
l.append(1)
print(list(l))

print(l)

l.popleft()
l.popleft()
print(list(l))