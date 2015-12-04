N,M = map(int, raw_input().split())

edge = []
weight = []

for i in xrange(M):
    x,y,r = map(int, raw_input().split())
    edge.append([x,y])
    weight.append(r)
start = int(raw_input())

#print edge
#print weight

##sort--Insertion Sort . could be better

for i in xrange(1,M):
    keyWeight = weight[i]
    keyEdge = edge[i]

    j=i-1
    while j>=0 and weight[j]>keyWeight:
        weight[j+1]= weight[j]
        edge[j+1]= edge[j]
        j=j-1
    edge[j+1] = keyEdge
    weight[j+1] = keyWeight

#print "sorted edges & weights"

#print edge
#print weight

#union find

class Node:
    def __init__(self,label):
        self.label = label
    def __str__(self):
        return self.label

def MakeSet(x):
    x.parent =x
    x.rank =0
    return

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
    return

def Find(x):
    if x.parent == x:
        return x
    else:
        return Find(x.parent)



l = [Node(i+1) for i in xrange(N)]

for i in xrange(N):
    MakeSet(l[i])

#Kruskals

ans =[]

for i in xrange(M):
    if i<M-1:
        if weight[i] == weight[i+1]:
            ui, vi = edge[i]
            un, vn = edge[i+1]
            costI = ui + vi + weight[i]
            costN = un + vn + weight[i+1]
            if costN < costI:
                tempWeight = weight[i+1]
                tempEdge = edge[i+1]
                weight[i+1]=weight[i]
                edge[i+1]=edge[i]
                weight[i]=tempWeight
                edge[i]=tempEdge

    v1,v2 = edge[i]
    w1 = weight[i]

    if Find(l[v1-1]) != Find(l[v2-1]):
        ans.append([v1,v2,w1])
        Union(l[v1-1],l[v2-1])

#print "Spanning Tree"
#print ans

cost = 0
for vertices in ans:
    cost += vertices[2]

print cost
