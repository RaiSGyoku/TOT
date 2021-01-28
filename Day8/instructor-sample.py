# OOP

class Car:
    color = "red"
    model = "SUV"
    manufacturer = "Toyota"


truck = Car()
van = Car()
jeepney = Car()

print(f"the truck color is: {truck.color}")
print(f"the truck model is: {truck.model}")
print(f"the truck manufacturer is: {truck.manufacturer}")

print(f"the jeep color is: {jeepney.color}")

van.color = "blue"
van.manufacturer = "Honda"
print(f"the van color is: {van.color}")
print(f"the van manufacturer is: {van.manufacturer}")