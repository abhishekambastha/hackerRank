class heap:
    def __init__(self, A):
        self.heapsize = len(A)
        self.A = A
        for i in xrange((self.heapsize/2),-1,-1):
            self.Heapify(i)


    def Parent(self,i):
        return (i+1)/2-1

    def Left(self,i):
        return 2*i+1

    def Right(self,i):
        return 2*i+2

    def Heapify(self,i):
        smallest=0
        l = self.Left(i)
        r = self.Right(i)

        if l<self.heapsize and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r<self.heapsize and self.A[r] < self.A[smallest]:
            smallest = r

        if smallest != i:
            temp = self.A[i]
            self.A[i] = self.A[smallest]
            self.A[smallest] = temp
            self.Heapify(smallest)

    def BuildHeap(self,A):
        self.heapsize = len(A)
        self.A = A
        for i in xrange((self.heapsize/2),-1,-1):
            self.Heapify(i)

    def ExtractMin(self):
        minVal = self.A[0]
        self.BuildHeap(self.A[1:])
        return minVal

A = [16,14,10,7,14,3,0,1,2,8]
h = heap(A)


print h.A

for i in xrange(9):
    print "Extracting Min"
    h.ExtractMin()
    print h.A
    print "\n"
