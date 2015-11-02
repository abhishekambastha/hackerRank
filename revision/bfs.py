import sys
import Queue

adjList = {"r":["s","v"], "s":["r","w"],"t":["w","x","u"], "u":["x","y"],"v":["r"],"w":["s","t","x"]\
           , "x":["w","t","u","y"],"y":["x","u"]}

color = {}
dist = {}

#Initialize distance and color
for node in adjList:
    color[node] = "white"
    dist[node] = sys.maxint

dist["r"] = 0
que = Queue.Queue()
que.put("r")

while que.empty() == False:
    node = que.get()
    print node
    for childNode in adjList[node]:
        if color[childNode] == "white":
            color[childNode] = "gray"
            dist[childNode] = dist[node] +1
            que.put(childNode)
    color[node] = "black"

print dist 
