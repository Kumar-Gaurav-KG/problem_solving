'''
given a number, generate spiral matrix,
ex n=3
[1 2 3
 8 9 4
 7 6 5]
 '''

def generateMatrix(A):
    mat = [[0 for _ in range(A)] for _ in range(A)]
    count = 1
    i = 0
    j = 0
    n = A
    while(A>1):
        
        print(A)
        for k in range(0,A-1):
            mat[i][j] = count
            count+=1
            print(i,j)
            j+=1
            
        for k in range(0,A-1):
            mat[i][j] = count
            count+=1
            print(i,j)
            i+=1
        for k in range(0,A-1):
            mat[i][j] = count
            count+=1
            print(i,j)
            j-=1
        for k in range(0,A-1):
            mat[i][j] = count
            count+=1
            print(i,j)
            i-=1
    

        A=A-2
        i+=1
        j+=1
    if A==1:
        mat[i][j] = count
    
    return mat

a = generateMatrix(4)
for x in range(len(a)):
    for j in range(len(a[0])):
        print(a[x][j],end=' ')
    print('\n')