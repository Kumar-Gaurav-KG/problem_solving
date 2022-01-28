def solve(A):
    pfeodd =[0 for x in range(len(A))]
    pfeven =[0 for x in range(len(A))]

    pfeven[0] = A[0]
    pfeodd[0] = 0
    for x in range(1,len(A)):
        if x%2==0:
            pfeven[x] = pfeven[x-1] + A[x]
        else:
            pfeven[x] = pfeven[x-1]

    for x in range(1,len(A)):
        if x%2!=0:
            pfeodd[x] = pfeodd[x-1] + A[x]
        else:
            pfeodd[x] = pfeodd[x-1]
    print(A)
    print(pfeodd, pfeven)

    c =0
    for y in range(0, len(A)):
        if y==0:
            oddsum = pfeven[len(A)-1] - pfeven[0]
            evensum = pfeodd[len(A)-1] - pfeodd[0]
        else:
            oddsum = pfeodd[y-1] + (pfeven[len(A)-1] - pfeven[y])
            evensum = pfeven[y-1] + (pfeodd[len(A)-1] - pfeodd[y])
        print(oddsum, evensum)
        if oddsum == evensum:
            c+=1

    return c

solve([2, 1, 6, 4])