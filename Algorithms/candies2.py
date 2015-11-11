N = int(raw_input())
student = {}
candy = {}

for i in xrange(N):
    student[i] = int(raw_input())
    candy[i] =1

for i in xrange(1,N):
    if student[i] > student[i-1]:
        candy[i] = candy[i-1]+1
for i in xrange(N-2,-1,-1):
    if student[i] > student[i+1]:
        candy[i] = max(candy[i], candy[i+1]+1)

totalcandy =0
for i in xrange(N):
    totalcandy += candy[i]

print totalcandy

