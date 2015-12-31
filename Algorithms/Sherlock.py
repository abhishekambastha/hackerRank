TestCases = int(raw_input())


def sol(arr):
    l = len(arr)
    if l==1:
        return True

    front = [-1 for i in xrange(l)]
    back = [-1 for i in xrange(l)]
    front[0] = arr[0]
    back[l-1] = arr[l-1]
    for i in xrange(1,l):
        front[i] = front[i-1]+arr[i]

    for i in xrange(l-2,-1,-1):
        back[i] = back[i+1]+arr[i]

    ans = False
    for i in xrange(l-2):
        if front[i] == back[i+2]:
            ans = True
            break

    return ans

for p in xrange(TestCases):
    ignore = int(raw_input())
    arr = map(int, raw_input().strip().split())
    ans = sol(arr)

    if ans:
        print "YES"
    else:
        print "NO"
