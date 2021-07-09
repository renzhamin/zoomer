from aliases import mp
from datetime import datetime
from functools import cmp_to_key
from importlib import import_module
from datatypes import Post
import re

def importTodaysClasses():
    mpday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saterday","Sunday"]
    _ = import_module(f'Routine.{mpday[datetime.now().weekday()]}')
    return _.classes

def sortClasses(classlist):
    today = datetime.now()
    h = today.hour + today.minute/60.0

    def compare(a,b):
        if a.hour>=h and b.hour>=h:
            return a.hour - b.hour
        if a.hour<h and b.hour>=h:
            return 1
        if a.hour<b.hour or (a.hour>=h and b.hour<h):
            return -1
        return 1

    classlist.sort(key=cmp_to_key(compare))
    return classlist


def getCurrentClasses(classlist):
    if classlist is None: return []
    classlist = sortClasses(classlist)
    current = [classlist[0]]
    if len(classlist)>1 and classlist[1].hour == classlist[0].hour:
        current.append(classlist[1])
    return current

def getUpdateTime(d):
    if not d:return ' '
    diff=datetime.now()-datetime.strptime(d,'%Y-%m-%dT%H:%M:%S.%fZ')
    hours,rem=divmod(diff.total_seconds()-diff.days*24*3600,3600)
    minutes=divmod(rem,60)[0]
    return f'[ {diff.days} day,{int(hours)} hour,{int(minutes)} min ago ]'


def link(course,service):
    if course.link != '404':
        return [course.link],' '
    results = service.courses().announcements().list(courseId=course.id,pageSize=4).execute().get('announcements',[])
    results = str(results)
    x = course.pattern.search(results)
    y = ' '
    if x:
        y=re.search(r"'updateTime': '(\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z)'",results[x.start():])
        if y:y=getUpdateTime(y.group(1))

    if not course.matchMoreThanOnce:
        if not x:x=' '
        else: x=[x.group()]
        return x,y

    x = course.pattern.findall(results)
    if not x: x = ['404']
    elif len(x)>2: x=x[:2]
    return x,y


def getClassLinks(service,classlist):
    s=""
    for i in classlist:
        x,y = link(i.inf,service)
        s+=f'<div class="name">{i.inf.name} {y}</div>'
        for j in x:
            s+=f'<a href={j} target="_blank">{j}</a><br>'
        s+=f'<div class="duration">From {i.startTime} to {i.endTime}</div><br>'
    return s


def getAllLinks(service):
    s=""
    for i in mp.values():
        s+=f'<div class="name">{i.name}</div>'
        x = link(i,service)
        for j in x:
            s+=f'<a href={j} target="_blank">{j}</a><br>'
        s+='<br>'
    return s


def postLists(service):
    ls=[]
    for i in mp.values():
        results = service.courses().announcements().list(courseId=i.id,pageSize=2).execute().get('announcements',[])
        ls.append(Post(i.name,results[0]['text'],results[0]['updateTime']))
    ls.sort(key=lambda Post:Post.date,reverse=True)
    sz=min(10,len(ls))
    ls=ls[:sz]
    return ls



def showPosts(postList):
    s=''
    for i in postList:
        s+=f'<div class="name">{i.name} {getUpdateTime(i.date)}</div><p>{i.text}</p>'
    return s
