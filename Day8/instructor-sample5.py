# Protected Access Modifiers

class Person:
    def __init__(self, name, age):
        self._Pname = name # single underscore means protected in python
        self.PAge = age

    def displayAge(self):
        print(f"Age {self.PAge}")

obj = Person("Julien", 20)
print(f"Name {obj._Pname}")
obj.displayAge()