N = int(raw_input())
student = {}
candy = {}
for i in xrange(N):
    student[i] = int(raw_input())
    candy[i] = 1

totalCandy =0
for i in xrange(1,N-1):
    if student[i] > student[i+1]:
        while candy[i] <= candy[i+1]:
            candy[i] = candy[i+1]+1

    if student[i] > student[i-1]:
        while candy[i] <= candy[i-1]:
            candy[i] = candy[i-1]+1

#Case 0
if student[0] > student[1]:
    while candy[0] <= candy[1]:
        candy[0] = candy[1]+1
#case N-1

if student[N-1] > student[N-2]:
    while candy[N-1] <= candy[N-2]:
        candy[N-1] = candy[N-2]+1

for i in xrange(0,N):
    totalCandy += candy[i]



print totalCandy
