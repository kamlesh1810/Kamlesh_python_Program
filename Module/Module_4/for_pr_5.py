def fun(fileName ):
    with open(fileName) as f:
        content=f.readlines()
    print(content)

fun('firstN_Line.txt')


