class Tuple():
    def usng_len_Function():
        MyAnime = ('Naruto', 'Babidi', 'Doreamon','conan')
        print(len(MyAnime)) #count the item inside of the tuple

    def usng_max_Function():
        myGrade = (89,90,92,89,87)
        print(max(myGrade)) #getting the highest value in the tuple

    def basic_sample():
        tup1 = ('physical','chemistry',1997,2000)
        tup2 = (1,2,3,4,5,6,7)
        
        print("tup1[0]:", tup1[0])
        print("tup2[1:5]:", tup2[1:5]) # name of tuple[index:range] 
        
        print(f"tup2[1:len(tup2): {tup2[1:len(tup2)]}") #can be use as well 


class Dictionary():
    pass

Tuple.usng_len_Function()
Tuple.usng_max_Function()