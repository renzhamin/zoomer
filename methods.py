from currentClasses import curClasses
from datetime import datetime,timedelta
from datatypes import Post
from aliases import mp
import re

def getUpdateTime(d):
    if not d:return ' '
    diff=(datetime.now()-timedelta(hours=6))-datetime.strptime(d,'%Y-%m-%dT%H:%M:%S.%fZ')
    hours,rem=divmod(diff.total_seconds()-diff.days*24*3600,3600)
    minutes=divmod(rem,60)[0]
    return f'[ {diff.days} day,{int(hours)} hour,{int(minutes)} min ago ]'

def link(course,service,noOfPostsToCheck=4,raw=0):
    if course.link != '404':
        return [course.link],' '
    results = service.courses().announcements().list(courseId=course.id,pageSize=noOfPostsToCheck).execute().get('announcements',[])

    if raw:
        return results

    results = str(results)
    x = course.pattern.search(results)
    y = ' '
    if x:
        y=re.search(r"'updateTime': '(\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z)'",results[x.start():])
        if y:y=getUpdateTime(y.group(1))

    if course.numberofMatches==1:
        if not x:x=['404']
        else: x=[x.group()]
        return x,y

    x = course.pattern.findall(results)
    if not x: x = ['404']
    else: x=x[:min(len(x),course.numberofMatches)]
    return x,y


def getClassLinks(service):
    classlist = curClasses()
    for i in classlist:
        x,y = link(i.inf,service)
        x = '\n'.join(x)
        print(f'{i.inf.name} {y}\n{x}\nFrom {i.startTime} to {i.endTime}\n')


def getCourseIds(service):
    results = service.courses().list().execute()
    courses = results.get('courses',[])
    x = ""
    for i in courses:
        x+=f'Course Name\t: {i["name"]}\nCourse ID\t:{i["id"]}\n----------------------------------------------------\n'
    f = open('FetchedCourseIds','w')
    f.write(x)
    f.close()
    print(x)

def postLists(service,courseList=mp.values(),noOfPosts=4,postPerCourse=2):
    ls=[]
    for i in courseList:
        results = service.courses().announcements().list(courseId=i.id,pageSize=postPerCourse).execute().get('announcements',[])
        for j in range(min(len(results),postPerCourse)):
            ls.append(Post(i.name,results[j]['text'],results[j]['updateTime']))
    ls.sort(key=lambda Post:Post.date,reverse=True)
    sz=min(noOfPosts,len(ls))
    ls=ls[:sz]
    return ls



def showPosts(postList,multi=1):
    s=''
    for i in postList:
        if multi: s+=f'{i.name} '
        s+=f'{getUpdateTime(i.date)}\n{i.text}\n\n'
    return s
