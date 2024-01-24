personaldata = {"Name" : "Luckyta Afia Susanto",
                "NIM" : "L200183103",
                "Address" : "-",
                "Majors" : "Double Degree of Informatics Engineering",
                "Faculty" : "FKI",
                "Religion" : "-",
                "Hobby" : "-"}
def Name():
    print (personaldata["Name"])
def NIM():
    print (personaldata["NIM"])
def Address():
    print (personaldata["Address"])
def Majors():
    print (personaldata["Majors"])
def Faculty():
    print (personaldata["Faculty"])
def Religion():
    print (personaldata["Religion"])
def Hobby():
    print (personaldata["Hobby"])

def x():
    print ("""Option Available:
-x Display the Choice
-1 Display the Name
-2 Display the NIM
-3 Display the Address
-4 Display the Majors
-5 Display the Faculty
-6 Display the Religion
-7 Display the Hobby
-c Close the Program""")
x()

while True:
    y = input("Your Choice: ")
    if y == "x":
        x()
    elif y == "1":
        Name()
    elif y == "2":
        NIM()
    elif y == "3":
        Address()
    elif y == "4":
        Majors()
    elif y == "5":
        Faculty()
    elif y == "6":
        Religion()
    elif y == "7":
        Hobby()
    elif y == "c":
        print ("The Program is closed")
        break
    else:
        print ("Invalid")
        
