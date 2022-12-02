try:
    # f=open("C:\Users\Dell\Documents\GitHub\Kamlesh_python_Program\Module\Module_4\txt file\file.txt",'r')

    f=open("file.txt",'r')
    print(f.read())
    f.close()

except FileNotFoundError:
    print("Plz check the path")