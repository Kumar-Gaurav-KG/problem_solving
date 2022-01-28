def rangeSum(A, B):
    result = []
    prefixsum = [0 for x in range(len(A))]
    #print(prefixsum)
    prefixsum[0] = A[0]
    #print(prefixsum)
    for i in range(1,len(A)):
        prefixsum[i] = prefixsum[i-1] + A[i]
    print(prefixsum)
    for j in B:
        if j[0]-1 == 0:
            result.append(prefixsum[j[1]-1])
        else:
            end = j[1]-1
            start = j[0]-1
            s = prefixsum[end]- prefixsum[start-1]
            print(s)
            result.append(prefixsum[end]- prefixsum[start-1])

    return result

print(rangeSum([ 7, 3, 1, 5, 5, 5, 1, 2, 4, 5 ], [[7, 10],[3, 10],[3, 5],[1, 10]]
))