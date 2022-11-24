li = [(1, 2, 3, 4), (), "Hello", (), ('a', 'b', 'c'), ('', ''), ()]
print(li, "\n")

for i in li:
    if len(i) == 0:
        li.remove(i)
print(li)
