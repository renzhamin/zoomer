from classroomapi import auth
from flask import Flask
from methods import importTodaysClasses,getCurrentClasses,getAllLinks,getClassLinks,showPosts,postLists

app = Flask(__name__)
service = auth()
classlist = importTodaysClasses()

style = '''
    <head>
    <style>
    body {
        background-color : #191a1b;
        color : white;
        font-size : 1.6em;
    }
    a{
        color : #eb344f;
        text-decoration : none;
    }
    .name{
        color : #34a2eb;
    }
    .duration{
        color : #a1b0c2;
    }
    p{
        color : #f2f0d5;
    }
    </style>
    </head>
'''

getTodayshtml = '<br><a href="/today">Get links for todays classes</a><br>'
getAllhtml = '<br><a href="/all" target="_blank">Get links for all courses</a><br>'
getFeedhtml = '<br><a href="/posts" target="_blank">Get recent posts</a><br>'

@app.route('/all')
def getAll():
    return (style + getAllLinks(service))

@app.route('/today')
def getTodaysClasses():
    return (style + getClassLinks(service,classlist) + getFeedhtml + getAllhtml)
   
@app.route('/')
def now():
    return (style + getClassLinks(service,getCurrentClasses(classlist)) + getFeedhtml +getTodayshtml + getAllhtml)

@app.route('/posts')
def getFeed():
    return (style + showPosts(postLists(service)))

if __name__=='__main__':
    app.run(debug=True)
