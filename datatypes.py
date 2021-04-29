from datetime import datetime

class Course:
    def __init__(self,name,id,link="404"):
        self.name=name
        self.link=link
        self.id=id


class Class:
    def __init__(self,inf,starth,startm,endh,endm):
        self.inf=inf
        self.endm=endm
        self.endh=endh
        self.hour=endh+endm/60.0
        self.starth=starth
        self.startm=startm
        self.messege=""
        self.startTime=datetime.strptime(f'{starth}:{startm}',"%H:%M").strftime("%I:%M %p")
        self.endTime=datetime.strptime(f'{endh}:{endm}',"%H:%M").strftime("%I:%M %p")
