from currentClasses import curClasses
from re import findall

def link(ID,service,parse=0,post=0):
    results = service.courses().announcements().list(courseId=ID).execute().get('announcements',[])

    if post:
        return results[0]['text']

    for i in results:
        x = findall(r'(https\S+zoom\S+)',i['text'])
        if not x:
            try:
                x = findall(r'(https\S+zoom\S+)',i['materials'][0]['link']['url'])
            except:
                pass
        if x: return x if parse else i['text']
    return None


def getClassLinks(service):
    classlist = curClasses()
    for i in classlist:
        x = i.inf.link
        if x=='404':
            x = link(i.inf.id,service,parse=1)
            if x: x='\n'.join(x)
            else: x='404'
        print(f'{i.inf.name}\n{x}\nFrom {i.startTime} to {i.endTime}\n')


def getCourseIds(service):
    results = service.courses().list().execute()
    courses = results.get('courses',[])
    x = ""
    for i in courses:
        x+=f'Course Name\t: {i["name"]}\nCourse ID\t:{i["id"]}\n----------------------------------------------------'
    f = open('FetchedCourseIds','w')
    f.write(x)
    f.close()
    print(x)
