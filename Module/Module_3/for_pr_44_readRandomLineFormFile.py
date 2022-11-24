import random
# f=open("text.txt",'w')
# f.write("Hello Dear")
# f.write("\nGood morning")
# f.write("\nHow are you")
# f.write
# f.close()
def ran_line(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)
print(ran_line('text.txt')) 