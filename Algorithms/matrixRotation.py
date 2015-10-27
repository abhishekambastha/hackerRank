inp = raw_input()
M, N, R = map(int,inp.split())

mat=[]
for i in range(M):
    rows = map(int, raw_input().split())
    mat.append(rows)

layer = min(M,N)/2
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotateAntiClock(matrix,layer, M,N,R):

    for L in range(layer):
        rot = R % (2*M+2*N-8*L-4)
        for i in range(rot):
            topLeft = matrix[0+L][0+L]
            topRight = matrix[0+L][N-L-1]
            bottomLeft = matrix[M-1-L][0+L]
            bottomRight = matrix[M-1-L][N-1-L]
            #top
            for i in range(L,N-L-1):
                matrix[L][i] = matrix[L][i+1]

            #left
            for i in range(M-L-1,L,-1):
                matrix[i][L] = matrix[i-1][L]
            matrix[L+1][L] = topLeft

            #bottom
            for i in range(N-L-1,L,-1):
                matrix[M-L-1][i]= matrix[M-L-1][i-1]
            matrix[M-L-1][L+1] = bottomLeft

            #right
            for i in range(L,M-L-1):
                matrix[i][N-L-1] = matrix[i+1][N-L-1]
            matrix[M-L-2][N-L-1] = bottomRight


    return matrix

def printMatrix(matrix):
    for row in matrix:
        string =""
        for element in row:
           string = string + str(element) + "\t"
        print string



#printMatrix(matrix)
#ans = rotateAntiClock(matrix,layer)
#printMatrix(ans)

ans = rotateAntiClock(mat,layer,M,N,R)

printMatrix(ans)
