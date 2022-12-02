def fun(fileName):
    with open(fileName) as f:
        var=f.readlines()
        print(var)


fun('firstN_Line.txt')