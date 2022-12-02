"""
 __init__ ():
 
  It is the constructor function for the classes in Python. The def keyword is used to define it because it’s a function. The first argument refers to the current object. It binds the instance to the init () method. It’s usually named “self” to follow the naming convention.
  Always called when an object is created

  def __init__(self):
    # body of the constructor

"""


class Demo:
    def __init__(self) -> None:
        print("This is constructor function called")

obj=Demo()

