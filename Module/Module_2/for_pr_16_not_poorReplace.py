# str="and not be poor and broke	"
str=input("Enter a string that contains a 'not' and a 'poor' word for it: ")
sNot = str.find("not")
sPoor = str.find("poor")

if sPoor > sNot and sNot > 0 and sPoor > 0:
    str = str.replace(str[sNot:(sPoor+4)], 'good')
    print(str)
else:
    print("Plz enter another string in which 'not' follows the 'poor'")    
