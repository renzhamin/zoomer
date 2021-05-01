from classroomapi import auth
from aliases import mp
from sys import argv
import methods

def main():
    service = auth()
    if len(argv)==1:
        methods.getClassLinks(service)
    elif argv[1]=="1":
        methods.getCourseIds(service)
    else:
        if argv[1] not in mp:
            print("No such class")
            return
        if len(argv)==2:
            x = methods.link(mp[argv[1]].id,service,parse=1)
            print('\n'.join(x))
        else:
            print(methods.link(mp[argv[1]].id,service,post=(argv[2]=='post')))

if __name__=='__main__':
    main()
