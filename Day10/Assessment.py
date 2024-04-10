#try:

def file_Loc():
    return("Day10/ReservatoinRecord.txt")
class Reservation():
    def MakeReservation(self):
        a = 1
        f = open(file_Loc(),"r")
        lines = f.readlines()
        for i in lines:
            a += 1
        reservKey= "Rev"+str(a)
        reserv_info = (f"{reservKey} {self.reservation_date} {self.reservation_time} {self.customer_name} {self.noOfAdult} {self.noOfChildren} {Reservation.compute(self)} \n")
        file = open(file_Loc(), "a")
        file.write(reserv_info)
        file.close()
    def RemoveReservation(self):
        a_file =open(file_Loc(),"r")
        lines = a_file.readlines()
        a_file.close()
        new_file= open(file_Loc(),"w")
        for line in lines:
            if line.strip("\n") != self.revkey:
                new_file.write(line)
        new_file.close()
    def compute(self):
        pricePerAdult = 500
        pricePerChildren = 300
        adultSubtotal = pricePerAdult * self.noOfAdult
        childSubtotal = pricePerChildren * self.noOfChildren
        subtotal = adultSubtotal + childSubtotal
        return (subtotal)
    def displayReservation(self):
        f = open(file_Loc(),"r")
        lines=f.readlines()
        listName = []
        listDate0 = []
        listDate1 = []
        listDate2 = []
        listTime0 = []
        listTime1 = []
        listAdult = []
        listChild = []
        listtotal = []
        for i in lines:
            listDate2.append(i.split(" ")[3])
            listDate1.append(i.split(" ")[2])
            listDate0.append(i.split(" ")[1])
            listTime0.append(i.split(" ")[4])
            listTime1.append(i.split(" ")[5])
            listName.append(i.split(" ")[6])
            listAdult.append(i.split(" ")[7])
            listChild.append(i.split(" ")[8])
            listtotal.append(i.split(" ")[9])
        f.close() 
        a = 0
        for i in lines:
            newName = str(listName[a]).replace("_", " ")
            print(f"{listDate0[a]} {listDate1[a]} {listDate2[a]} {listTime0[a]} {listTime1[a]} {newName} {listAdult[a]} {listChild[a]}")
            a+=1        
    def GenerateReport(self):
        f = open(file_Loc(),"r")
        lines=f.readlines()
        listName = []
        listDate0 = []
        listDate1 = []
        listDate2 = []
        listTime0 = []
        listTime1 = []
        listAdult = []
        listChild = []
        listtotal = []
        for i in lines:
            listDate2.append(i.split(" ")[3])
            listDate1.append(i.split(" ")[2])
            listDate0.append(i.split(" ")[1])
            listTime0.append(i.split(" ")[4])
            listTime1.append(i.split(" ")[5])
            listName.append(i.split(" ")[6])
            listAdult.append(i.split(" ")[7])
            listChild.append(i.split(" ")[8])
            listtotal.append(i.split(" ")[9])           
        f.close()
        newListchild = []
        newListAdult = []
        newTotal = []
        for i in listChild:
            newListchild.append(int(i))
        for i in listAdult:
            newListAdult.append(int(i))
        for i in listtotal:
            newTotal.append(int(i))
        a = 0
        for i in lines:
            newName = str(listName[a]).replace("_", " ")
            print(f"{listDate0[a]} {listDate1[a]} {listDate2[a]} {listTime0[a]} {listTime1[a]} {newName} {listAdult[a]} {listChild[a]} {listtotal[a]}")
            a+=1  
        print(f"\nTotal number of Adults: {sum(newListAdult)}")
        print(f"Total number of Kids: {sum(newListchild)}")
        print(f"Grand Total: PHP {sum(newTotal)}")
        print("----------------------Nothing Follows----------------------")
###
class Reservation_info(Reservation):
    def __init__(self, name,date,time,noAdult,noChildren):
        self.customer_name = name
        self.reservation_date = date
        self.reservation_time = time
        self.noOfAdult = noAdult
        self.noOfChildren = noChildren

class Reservation_key(Reservation):
    def __init__(self, key):
        self.revkey = key
###
def is_empty(name, date, time, no_adult, no_child ):
    obj =Reservation()
    if name == '' or date == '' or time == '' or no_adult == ''or no_child == '':
        ValueError()
    else:
        obj = Reservation_info(str(name).replace(" ","_"), str(date), str(time), int(no_adult),  int(no_child))
        obj.MakeReservation()

def test():
    inpChoice = input("Enter no.1 for View All Reservations\nEnter no.2 for Make Reservation\nEnter no.3 for Delete Reservation\nEnter no.4 for Generate Report\nEnter no.5 for Exit\n Input: ")
    if int(inpChoice) == 1:
        obj =Reservation()
        obj.displayReservation()
    elif int(inpChoice) == 2:
        inpName = input("Customer Name: ")
        inpDate = input("Date of Reservation MMMMddyyyy: ")
        inpTime = input("Time of Reservation HH:mm XM: ")
        inpNoAdult = input("No. of Adult: ")
        inpNoChild = input("No. of Child: ")
        is_empty(inpName,inpDate,inpTime,inpNoAdult,inpNoChild)
    elif int(inpChoice) == 3:
        inpKey = input("Enter Reservation Key: ")
        obj =Reservation_key(inpKey)
        obj.RemoveReservation()
    elif int(inpChoice) == 4:
        obj =Reservation()
        obj.GenerateReport()
    elif int(inpChoice) ==5:
        print("Thank you")
    else:
        print("your input is not in the choices")
      
test()

####       
#except TypeError:
#    print("Invalid Input")
#except (ValueError):
#    print("Invalid Input")    