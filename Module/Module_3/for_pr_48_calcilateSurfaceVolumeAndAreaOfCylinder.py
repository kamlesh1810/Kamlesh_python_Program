pi=3.14
# pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
vol = pi * radian * radian * height
area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", vol)
print("Surface Area is: ", area)