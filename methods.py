from currentClasses import curClasses

def link(course,service,post=0):
    if course.link != '404':
        return [course.link]
    results = service.courses().announcements().list(courseId=course.id,pageSize=7).execute().get('announcements',[])
    if post:
        return results[0]['text']    
    results = str(results)
    if not course.matchMoreThanOnce:
        return [course.pattern.search(results).group()]
    x = course.pattern.findall(results)
    if not x: return ['404']
    if len(x)>2: x=x[:2]
    return x


def getClassLinks(service):
    classlist = curClasses()
    for i in classlist:
        x = link(i.inf,service)
        x = '\n'.join(x)
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
