import Queue
import sys

def initGraph():
    gr = {}
    N, M = map(int, raw_input().split())
    for i in range(N):
        gr[str(i+1)] = []

    for i in range(M):
        lis = raw_input().split()
        gr[lis[0]].append(lis[1])
        gr[lis[1]].append(lis[0])
    return gr

def printGraph(G):
    for keys in G.keys():
        print keys, ": ", G[keys]


def bfs(G,s):
    color = {}
    dist = {}
    for key in G.keys():
        color[key] = "white"
        dist[key] = sys.maxint

    color[s] = "gray"
    dist[s] = 0

    Q = Queue.Queue()
    Q.put(s)

    while not Q.empty():
        node = Q.get()
        for childNode in G[node]:
            if color[childNode] == "white":
                color[childNode] = "gray"
                dist[childNode] = dist[node] + 6
                Q.put(childNode)
        color[node] = "black"

    ans = ""
    for i in range(1,len(dist)+1):
        if not str(i) == s:
            if dist[str(i)] == sys.maxint:
                dist[str(i)] = -1

            ans += str(dist[str(i)]) + " "

    return ans


if __name__ == '__main__':
    testCases = int(raw_input())
    for i in range(testCases):
        g = initGraph()
        start = raw_input()
        ans = bfs(g,start)
        print ans
