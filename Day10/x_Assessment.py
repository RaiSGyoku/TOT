
class Reservation():
    def __init__(self, name,date,time,noAdult,noChildren):
        self.customer_name = name
        self.reservation_date = date
        self.reservation_time = time
        self.noOfAdult = noAdult
        self.noOfChildren = noChildren
    def MakeReservation(self):
        dict = {}
        #dict = {'Name': '', 'Date': '', 'Time':'','noAdult':,'noChild'}
        reservID = (f"{self.customer_name}{self.reservation_date}{self.reservation_time}")
        newReservID = reservID.replace(':', '')
        #reserv_info = (f"{newReservID.replace(' ', '')} {self.reservation_date} {self.reservation_time} {self.customer_name} {self.noOfAdult} {self.noOfChildren} \n")
        dict['id'] = newReservID.replace(' ', '')
        dict['name'] = self.customer_name
        dict['date'] = self.reservation_date
        dict['noAdult'] = self.customer_name
        dict['noChild'] = self.noOfChildren
        dict['subtotal'] = obj.compute()

    
        reserv_info = (f"{self.reservation_date} {self.reservation_time} {self.customer_name} {self.noOfAdult} {self.noOfChildren} {obj.compute()}\n")
        file = open("Day10/ReservatoinRecord.txt", "a")
        file.write(reserv_info)
        #file.write(str(dict))
        file.close()
        #print(dict)
    
    def RemoveReservation(self):
        #reservID = (f"{self.customer_name}{self.reservation_date}{self.reservation_time}")
        #newReservID = reservID.replace(':', '')
        
        reserv_info = (f"{self.reservation_date} {self.reservation_time} {self.customer_name} {self.noOfAdult} {self.noOfChildren} {obj.compute()}")
        r_file = open ("Day10/ReservatoinRecord.txt","r")
        lines = r_file.readlines
        
        file = open("Day10/ReservatoinRecord.txt","w")
        for line in lines:
            if line.strip("\n") != reserv_info:
                file.write(line)
        

    def compute(self):
        

    def displayReservation(self):
        file = open("Day10/ReservatoinRecord.txt","r")
        print (file.read())
        file.close()
    def GenerateReport(self):
        with open ("Day10/ReservatoinRecord.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.replace(line,''))

    
        



inpChoice = input("Enter no.1 for View All Reservations\nEnter no.2 for Make Reservation\nEnter no.3 for Delete Reservation\nEnter no.4 for Generate Report\nEnter no.5 for Exit\n Input: ")

if int(inpChoice) == 1:
    #file = open("Day10/ReservatoinRecord.txt","r")
    #print (file.read())
    #file.close()
    obj = Reservation('','','','','')
    obj.displayReservation()

elif int(inpChoice) == 2:
    inpName = input("Customer Name: ")
    inpDate = input("Date of Reservation: ")
    inpTime = input("Time of Reservation: ")
    inpNoAdult = input("No. of Adult: ")
    inpNoChild = input("No. of Child: ")

    obj = Reservation(str(inpName), str(inpDate), str(inpTime), int(inpNoAdult),  int(inpNoChild))
    obj.MakeReservation()

elif int(inpChoice) == 3:
    inpName = input("Customer Name: ")
    inpDate = input("Date of Reservation: ")
    inpTime = input("Time of Reservation: ")
    obj = Reservation(inpName, inpDate, inpTime, '',  '')
    obj.RemoveReservation()
elif int(inpChoice) == 4:
    obj = Reservation('', '', '', '',  '')
    obj.GenerateReport()


