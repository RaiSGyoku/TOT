# Private Access Modifiers
class Person:
    # constructor
    def __init__(self, name, age):
        # private data members
        self.__PName = name # double underscore for Private
        self.PAge = age

    def displayAge(self):
        # accessing public data member
        print (f"Age {self.PAge}")
    
    def displayName(self):
        # accessing Private data member
        print (f"Name {self.__PName}")

# creating object for the class
obj = Person("Julien", 20)

#print (f"Name: {obj.__PName}") #this ome is errored

# calling public member function of the class
obj.displayAge() # public
obj.displayName() # private
