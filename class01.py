id=0
def newid():
    global id
    id=id+1
    return id

class test1(object):
    def __init__(self,prop1):
        self.p1=prop1

class node(object):
    def __init__(self,sub):
        self.sub=sub
        self.id=newid()
