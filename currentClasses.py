from datetime import datetime
from functools import cmp_to_key
from importlib import import_module

mpday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saterday","Sunday"]

def curClasses():
    today = datetime.today()
    _ = import_module(f'Routine.{mpday[today.weekday()]}')
#     _ = import_module(f'Routine.{mpday[0]}')
    classlist = _.classes

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
