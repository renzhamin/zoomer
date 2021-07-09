from datetime import datetime
from re import compile

defaultPattern = compile(r'(https://bdren\.zoom\.us/j/[\d]+[?=\w\d]*)')

class Course:
    def __init__(self,name,id,link="404",pattern=defaultPattern,matchMoreThanOnce=0):
        self.name=name
        self.link=link
        self.id=id
        self.pattern=defaultPattern
        self.matchMoreThanOnce=matchMoreThanOnce


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

class Post:
    def __init__(self,name,text,date):
        self.name=name
        self.text=text
        self.date=date
