class Cellphone:
    color = ["red","blue","white","pink"]
    model = ["Galaxy A72","3310","moto G power","Zenfone 3 5.5"]
    manufacturer = ['Samsung','Nokia','Motolora','Asus']


Cellphone1 = Cellphone()
Cellphone2 = Cellphone()
Cellphone3 = Cellphone()
Cellphone4 = Cellphone()
Cellphone5 = Cellphone()

print(f"the Cellphone1 color is: {Cellphone1.color[0]}")
print(f"the Cellphone1 model is: {Cellphone1.model[0]}")
print(f"the Cellphone1 manufacturer is: {Cellphone1.manufacturer[0]}")
print("\n")
print(f"the Cellphone2 color is: {Cellphone2.color[1]}")
print(f"the Cellphone2 model is: {Cellphone2.model[1]}")
print(f"the Cellphone2 manufacturer is: {Cellphone2.manufacturer[1]}")
print("\n")
print(f"the Cellphone3 color is: {Cellphone3.color[2]}")
print(f"the Cellphone3 model is: {Cellphone3.model[2]}")
print(f"the Cellphone3 manufacturer is: {Cellphone3.manufacturer[2]}")
print("\n")
print(f"the Cellphone4 color is: {Cellphone4.color[3]}")
print(f"the Cellphone4 model is: {Cellphone4.model[3]}")
print(f"the Cellphone4 manufacturer is: {Cellphone4.manufacturer[3]}")

Cellphone5.color = "midnight blue"
Cellphone5.manufacturer = "Huawei"
Cellphone5.model = "Huawei"

print("\n")
print(f"the Cellphone5 color is: {Cellphone5.color}")
print(f"the Cellphone5 color is: {Cellphone5.color}")
print(f"the Cellphone5 manufacturer is: {Cellphone5.manufacturer}")