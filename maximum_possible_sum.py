'''
Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.'''

def solve(A, B):
    p = [0 for n in range(B)]
    s = [0 for n in range(B)]

    p[0] = A[0]
    s[0] = A[len(A)-1]

    for i in range(1,B):
        p[i] = p[i-1] + A[i]

    j =len(A)-2
    i=1
    while j>=len(A)-B:
        #print(A[j])
        s[i] = s[i-1] + A[j]
        j-=1
        i+=1

    print(s, p)

    maxx = max(p[B-1], s[B-1])

    for i in range(0,(B-1)):
        #print(p[i], s[B-2-i])
        if p[i]+s[B-2-i]> maxx:
            print(p[i]+s[B-2-i])
            maxx = p[i]+s[B-2-i]
            print(maxx)
    return maxx

solve([ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ], 48)