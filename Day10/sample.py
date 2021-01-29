#a_file = open("Day10/sampl.txt","r")
#lines =a_file.readlines()
#a_file.close()


#for line in lines:
#    count=0
#    if line == "sample3":
#        del line
        
#    count +=1     
    #else:
        #print(line)

#new_file = open("Day10/sampl.txt","w+")

#for line in lines:
#    new_file.write(line)

#new_file.close()



a_file =open("Day10/ReservatoinRecord.txt","r")

lines = a_file.readlines()
a_file.close()

new_file= open("Day10/ReservatoinRecord.txt","w")
for line in lines:
    if line.strip("\n") != "30 Oct 2020 10:00 am jasper 2 2 ":
        new_file.write(line)

new_file.close()





