#Snakes and Ladder
import sys
import Queue


def snakeLadderInput():
    snake = {}
    ladder = {}
    #Ladder
    numLadder = int(raw_input())
    for i in range(numLadder):
        lis = raw_input().split()
        ladder[lis[0]] = lis[1]

    numSnakes = int(raw_input())
    for i in range(numSnakes):
        lisSn = raw_input().split()
        snake[lisSn[0]] = lisSn[1]

    return [snake, ladder]



def snakeGraph(snake,ladder):
    adjList = {}
    temp = map(str, range(1,101))
    for i in range(1,101):
        if snake.has_key(str(i)):
            adjList[str(i)] = [snake[str(i)]]
        elif ladder.has_key(str(i)):
            adjList[str(i)] = [ladder[str(i)]]
        else:
            adjList[str(i)] = temp[i:i+6]
    return adjList


#bfs
def bfs(gr,snake,ladder):
    color = {}
    dist = {}

    for k in gr.keys():
        color[k] = "white"
        dist[k] = sys.maxint

    que = Queue.Queue()
    que.put("1")
    dist["1"] = 0
    color["1"] = "gray"

    while not que.empty():
        node = que.get()
        for childNode in gr[node]:
            if color[childNode] == "white":
                color[childNode] = "gray"
                if snake.has_key(node) or ladder.has_key(node):
                    dist[childNode] = dist[node] 
                else:
                    dist[childNode] = dist[node] + 1
                que.put(childNode)
        color[node] = "black"

    return dist["100"]


if __name__ == '__main__':
    testCases = int(raw_input())
    for i in range(testCases):
        snake, ladder = snakeLadderInput()
        gr = snakeGraph(snake, ladder)
        ans = bfs(gr, snake, ladder)
        if ans == sys.maxint:
            print "-1"
        else:
            print ans


