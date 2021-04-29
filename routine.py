from datetime import datetime
from datatypes import Class,Course

mp = {
# format is "classAlias" : Course("name of course","id","link")
# link is optional and if you want to auto update link from classroom dont set it to anything
# when you know a link doesnt change then you can set the link
# To get id run CL 1, a file named FetchedCourseIds in the project directory will be created containing ids for all your courses
    "ds" :  Course("Data Structures","325364815331"),
    "coa" :  Course("COA","324285830041"),
    "la" :  Course("Linear Algebra","317352830971"),
    "eee" :  Course("EEE","317485508357"),
    "eee_lab" :  Course("EEE_Lab","318097402722"),
    "dbms" :  Course("DBMS","318065155365","http://meet.google.com/ohp-mqxh-ndf"),
    "dbms_lab" :  Course("DBMS_Lab","317309193831"),
    "oop" :  Course("OOP","317199070205")
# "ds_lab" :  Course("Data Structures Lab","","https://bdren.zoom.us/j/67706040993")
# "oop_lab" :  Course("OOP Lab","404")
}

def curClasses():
    # forma for adding a Class to a day :
    # Class(mp["classAlias"],startTimeHour,startTimeMinue,endTimeHour,endTimeMinute)
    # for example,ds class at 12:30 to 13:30 (24 hour format)
    # Class(mp["ds"],12,30,13,30)

    Monday = [ 
        Class(mp["ds"],10,50,11,50),
        Class(mp["la"],12,0,13,0),
        Class(mp["eee"],13,30,14,30)
    ]


    Tuesday=[
       Class(mp["coa"],9,40,10,40),
       Class(mp["ds"],10,50,11,50),
       Class(mp["dbms"],12,0,13,0),
       Class(mp["eee_lab"],13,30,14,30)
    ]

    Wednesday=[
#    Class(mp["ds_lab"],9,40,10,40),
       Class(mp["dbms_lab"],9,40,10,40),
       Class(mp["dbms"],12,0,13,0),
       Class(mp["eee"],13,30,14,30)
    ]

    Thursday=[
       Class(mp["coa"],9,40,10,40),
       Class(mp["oop"],12,0,13,0),
#    Class(mp["oop_lab"],15,50,16,50)
    ]

    Friday=[
       Class(mp["dbms_lab"],9,40,10,40),
#    Class(mp["ds_lab"],9,40,10,40),
       Class(mp["la"],12,0,13,0),
       Class(mp["oop"],13,30,14,30),
#    Class(mp["oop_lab"],15,50,16,50)
    ]

    routine = [
       Monday,Tuesday,Wednesday,Thursday,Friday
    ]

    today = datetime.today().weekday()
    classlist = routine[today]

    return classlist
