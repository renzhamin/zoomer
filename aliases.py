from datatypes import Course

mp = {
# format is "classAlias" : Course(name of course,id,link,pattern=defaultPattern,matchMoreThanOnce=0)
# link is optional and if you want to auto update link from classroom dont set it to anything
# when you know a link doesnt change then you can set the link
# To get id run CL 1, a file named FetchedCourseIds in the project directory will be created containing ids for all your courses
# default pattern is a regex defined in datatypes.py
# if matchMoreThanOnce is 1 , 2 links will be provided
    "ds" :  Course("Data Structures","325364815331",matchMoreThanOnce=1),
    "coa" :  Course("COA","324285830041"),
    "la" :  Course("Linear Algebra","317352830971"),
    "eee" :  Course("EEE","317485508357"),
    "eee_lab" :  Course("EEE_Lab","318097402722"),
    "dbms" :  Course("DBMS","318065155365",link="http://meet.google.com/ohp-mqxh-ndf"),
    "dbms_lab" :  Course("DBMS_Lab","317309193831"),
    "oop" :  Course("OOP","317199070205"),
    "ds_lab" :  Course("Data Structures Lab","325364815331",matchMoreThanOnce=1)
# "oop_lab" :  Course("OOP Lab","404")
}
