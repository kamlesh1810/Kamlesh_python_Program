def add(x,y,z=0):
    return x+y+z

print("Adding only X and Y : ",add(12,1))    
print("Adding all variable's value : ",add(1,2,3))



# Polymorphism with a function and object

class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi id the most widely spoken language of India ")        
    def type(self):
        print("Inida is developing country")        

# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
  
# obj_ind = India()
# obj_usa = USA()
  
# func(obj_ind)
# func(obj_usa)