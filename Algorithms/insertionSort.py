def insertionSort(ar):
    for i in xrange(1,len(ar)):
        key = ar[i]
        j = i-1
        while j>=0 and ar[j] > key:
            ar[j+1]=ar[j]
            j = j-1
            printArr(ar)

        ar[j+1] = key
        if not j+1 == i:
            printArr(ar)
        
    return ""

def printArr(ar):
    s = ""
    for val in ar:
        s += str(val) + " "
    print s

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
