try:
    class house:
        def __init__(self,floorSize,noOfFloors,noOfDoors):
            self.floor_size = floorSize
            self.no_floors = noOfFloors
            self.no_doors = noOfDoors

        def isSwitchOn(self):
            return False

        def isLightOpen(self):
            if self.isSwitchOn() == True:
                return True
            else:
                return False
        def isOvenOpen(self):
            if self.isLightOpen() == True:
                return "LightOpen()\nOvenOpen()" 
            else:
                return False
    
        def displayAll(self):
            print (f"Floor size: {self.floor_size}\nNo of Floor: {self.no_floors}\nNo of Doors: {self.no_doors}\n{self.isOvenOpen()}")

    class townHouse(house):
        def isSwitchOn(self):
            return (True)
        
    inpFloor = input("Enter no of Floors: ")
    inpDoors = input("Enter no of Doors: ")
    test2 = townHouse(60, inpFloor,inpDoors)
    test2.displayAll()


    #test1 = house(6000, 100,50)
    #test1.displayAll()


except:
    print("invalid input")