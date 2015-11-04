A, B, N = map(int, raw_input().split())

d = {}
for i in xrange(N):
    d[i+1] = 0

d[1] = A
d[2] = B

for i in xrange(3,N+1):
    d[i] = d[i-1]**2 + d[i-2]

print d[N]
