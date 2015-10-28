testCases = int(raw_input())

for i in range(testCases):
    R, C = map(int, raw_input().split())
    mat=[]
    for j in range(R):
        List = [int(a) for a in raw_input()]
        #List = map(int, raw_input().split())
        mat.append(List)

    r, c = map(int, raw_input().split())
    targetMat=[]
    for j in range(r):
        #List = map(int, raw_input().split())
        List = [int(a) for a in raw_input()]
        targetMat.append(List)

    #print mat
    #print targetMat

    validCase = True
    ans = False
    count =0
    for rowOffset in range(R-r+1):
        if validCase ==False:
            validCase = True
        if count > 0:
            break
        for columnOffset in range(C-c+1):
            if validCase == False:
                validCase = True
            if count >0:
                break
            for i in range(r):
                if validCase == False:
                    break
                for j in range(c):
                    if targetMat[i][j] == mat[i+rowOffset][j+columnOffset]:
                        #true case
                        ans = True
                    else:
                        #quit this case (2 for loops)
                        ans = False
                        validCase = False
                        break
            if ans==True:
                count +=1
                ans = False

    if count > 0:
        print "YES"
    else:
        print "NO"


