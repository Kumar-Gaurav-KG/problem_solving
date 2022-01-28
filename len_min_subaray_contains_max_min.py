def solve(A):
    count = 100000000000000
    minn = min(A)
    maxx = max(A)

    for i in range(len(A)):
        if A[i] == minn:
            for j in range(i+1,len(A)):
                if A[j] == minn:
                    break
                elif A[j] == maxx:
                    print(A[i:j+1])
                    l = j-i+1
                    print(l)
                    if l<count:
                        count =l
        elif A[i]== maxx:
            for j in range(i+1,len(A)):
                if A[j] == maxx:
                    break
                elif A[j] == minn:
                    print(A[i:j+1])
                    l = j-i+1
                    print(l)
                    if l<count:
                        count =l
        print(count)
    
    return count

solve([ 814, 761, 697, 483, 981 ])