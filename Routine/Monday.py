from datatypes import Class,Course
from aliases import mp

classes = [ 
    Class(mp["ds"],10,50,11,50),
    Class(mp["la"],12,0,13,0),
    Class(mp["eee"],13,30,14,30)
]

# format for adding a Class to a day :
# Class(mp["classAlias"],startTimeHour,startTimeMinue,endTimeHour,endTimeMinute)
# for example,ds class at 12:30 to 13:30 (24 hour format)
# Class(mp["ds"],12,30,13,30)
