from datetime import datetime
from re import compile

defaultPattern = compile(r'(https://bdren\.zoom\.us/j/[\d]+[?=\w\d]*)')

class Course:
    def __init__(self,name,id,link="404",pattern=defaultPattern,numberofMatches=1):
        self.name=name
        self.link=link
        self.id=id
        self.pattern=defaultPattern
        self.numberofMatches=numberofMatches


class Class:
    def __init__(self,inf,starth,startm,endh,endm):
        self.inf=inf
        self.endm=endm
        self.endh=endh
        self.hour=endh+endm/60.0
        self.starth=starth
        self.startm=startm
        self.startTime=datetime.strptime(f'{starth}:{startm}',"%H:%M").strftime("%I:%M %p")
        self.endTime=datetime.strptime(f'{endh}:{endm}',"%H:%M").strftime("%I:%M %p")

# format for adding a Class to a day :
# Class(mp["classAlias"],startTimeHour,startTimeMinue,endTimeHour,endTimeMinute)
# for example,ds class at 12:30 to 13:30 (24 hour format)
# Class(mp["ds"],12,30,13,30)
# see files in Routine/ for complete examples

class Post:
    def __init__(self,name,text,date):
        self.name=name
        self.text=text
        self.date=date
