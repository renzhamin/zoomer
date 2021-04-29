from functools import cmp_to_key
from datatypes import Class,Course
from datetime import datetime
from csv import reader

mpday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saterday","Sunday"]
mp = {}

with open('CourseIdentifier') as csvfile:
    body = reader(csvfile)
    for i in body:
        mp[i[0]]=Course(i[1],i[2],i[3])

curdate = datetime.today()
curday = curdate.weekday()

classlist = []
filepath = f'Routine/{mpday[curday]}'

with open(filepath) as csvfile:
    body = reader(csvfile)
    for i in body:
        classlist.append(Class(mp[i[0]],int(i[1]),int(i[2]),int(i[3]),int(i[4])))

h = curdate.hour + curdate.minute/60.0

def compare(a,b):
    if a.hour>=h and b.hour>=h:
        return a.hour - b.hour
    if a.hour<h and b.hour>=h:
        return 1
    if a.hour<b.hour or (a.hour>=h and b.hour<h):
        return -1
    return 1

classlist.sort(key=cmp_to_key(compare))
