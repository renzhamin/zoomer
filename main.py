from classroomapi import auth
from aliases import mp
from sys import argv
import methods

def main():
    service = auth()
    if len(argv)==1:
        methods.getClassLinks(service)
    elif argv[1]=="id":
        methods.getCourseIds(service)
    else:
        if str(argv[1])=="post":
            postsToShow=5
            postPerCourseToConsider=2
            if len(argv)>2:
                postsToShow = int(argv[2])
            if len(argv)>3:
                postPerCourseToConsider = int(argv[3])
            print(methods.showPosts(methods.postLists(service,noOfPosts=postsToShow,postPerCourse=postPerCourseToConsider)))
            return
        if argv[1] not in mp:
            print("No such class")
            return
        if len(argv)==2:
            x,y = methods.link(mp[argv[1]],service)
            print(y,'\n','\n'.join(x))
        elif argv[2]=="raw":
            postsToShow = 5
            if len(argv)>3:
                postsToShow = int(argv[3])
            print(methods.link(mp[argv[1]],service,noOfPostsToCheck=postsToShow,raw=(argv[2]=='raw')))
            return
        elif argv[2]=="post":
            postsToShow=2
            if len(argv)>3:
                postsToShow = int(argv[3])
            print(methods.showPosts(methods.postLists(service,courseList=[mp[argv[1]]],noOfPosts=postsToShow,postPerCourse=postsToShow),multi=0))


if __name__=='__main__':
    main()
