class person:
    def __init__(self, fname, lname, email) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email

    def showDetails(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Email: ", self.email)


fname = input("Enter name: ")
lname = input("Enter last name: ")
email = input("Enter email: ")

obj = person(fname, lname, email)
obj.showDetails()
