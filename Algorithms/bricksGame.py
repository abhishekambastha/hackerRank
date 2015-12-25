testcases = int(raw_input())


def maximizescore(i):
    if i>=j:
        return 0
    if not sol[i]==-1:
        return sol[i]

    if (j-i)>5:
        ans = max (bricks[i]+min(maximizescore(i+2), maximizescore(i+3), maximizescore(i+4)) ,\
                   bricks[i]+bricks[i+1]+min(maximizescore(i+3), maximizescore(i+4), maximizescore(i+5)), \
                   bricks[i]+bricks[i+1]+ bricks[i+2]+ min(maximizescore(i+4), maximizescore(i+5), maximizescore(i+6)))
        sol[i] = ans
        return ans
    elif (j-i)==5:
        if(bricks[i+1]+bricks[i+2]) > (bricks[i+4]):
            sol[i] = bricks[i]+bricks[i+1]+bricks[i+2]
        else:
            sol[i] = bricks[i]+bricks[i+4]
    elif (j-i)==4:
        sol[i] = bricks[i]+bricks[i+1]+bricks[i+2]
    else:
        sol[i] = sum(bricks[i:])


for s in xrange(testcases):
    ignore = int(raw_input())
    bricks = map(int, raw_input().split())
    j = len(bricks)
    sol=[]
    for i in xrange(j):
        sol.append(-1)
    x = maximizescore(0)
    print x


