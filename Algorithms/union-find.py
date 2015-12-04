class Node:
    def __init__(self,label):
        self.label = label
    def __str__(self):
        return self.label

def MakeSet(x):
    x.parent =x
    x.rank =0

def Union(x,y):
    xRoot = Find(x)
    yRoot = Find(y)
    if xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    elif xRoot.rank < yRoot.rank:
        xRoot.parent = yRoot
    elif xRoot != yRoot:
        yRoot.parent = xRoot
        xRoot.rank += 1

def Find(x):
    if x.parent == x:
        return x
    else:
        return Find(x.parent)
