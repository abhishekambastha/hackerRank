import sys
testCases = int(raw_input())

def maxSum(a):
    currentSum = 0
    currentNonContiguousSum = 0
    maxSum = -1 * sys.maxint
    maxNonContiguousSum = maxSum

    for i in xrange(len(a)):
        currentElement = a[i]
        currentSum += currentElement
        if currentSum < 0:
            currentSum = 0
        if maxSum < currentSum:
            maxSum = currentSum
        #Non Cont. Case

        if currentNonContiguousSum < (currentNonContiguousSum + currentElement):
            currentNonContiguousSum += currentElement
        if maxNonContiguousSum < currentNonContiguousSum:
            maxNonContiguousSum = currentNonContiguousSum
    mx = max(a)
    if mx < 0:
        maxSum = mx
    if mx < 0:
        maxNonContiguousSum = mx
    return [maxSum, maxNonContiguousSum]

def maxNonContiguousSum(a):
    currentSum =0
    maxSum = -1 * sys.maxint

    for i in range(len(a)):
        if (currentSum + a[i]) > currentSum:
            currentSum += a[i]
        if maxSum < currentSum:
            maxSum = currentSum

        if max(a) > maxSum:
            maxSum = max(a)
    return maxSum

for i in range(testCases):
    l = int(raw_input())
    array = map(int, raw_input().split())
    ans, ans1 = maxSum(array)
    #ans1 = maxNonContiguousSum(array)
    print ans, ans1


