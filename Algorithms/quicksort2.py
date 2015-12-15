def partition(A,p,q):
    pivot = A[q]
    i = p-1
    for j in xrange(p,q):
        if A[j] < pivot:
            i = i+1
            swap(A,j,i)
    swap(A,i+1,q)
    return i+1

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def printArr(A):
    s = ""
    for c in A:
        s += str(c) + " "
    print s

def quickSort(A,p,q):
    if q-p>0:
        x = partition(A,p,q)
        printArr(A)
        quickSort(A,p,x-1)
        quickSort(A,x+1,q)
    else:
        pass

m = input()
ar = [int(i) for i in raw_input().strip().split()]

quickSort(ar,0,len(ar)-1)
