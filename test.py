
import math
class Solution:
    # @param A : integer
    # @return an integer
    def binary_search(self, n,i,e):
        mid = (i+e)/2
        print(mid)
        sq = mid*mid
        if (sq==n) or (abs(sq - n) < 0.00001):
            return mid
        else:
            if sq<n:
                return self.binary_search(n, mid, e)

            else:
                return self.binary_search(n, i, mid)
        
    def sqrt(self, A):
        i = 1
        f = True
        while(f):
            print(i*i, A)
            if i*i==A:
                return i
                f = False
            else:
                if (i*i>A):
                    res = self.binary_search(A,i-1,i)
                    f = False
                    return math.floor(res)

            i+=1

    def solve(self, A):
        swap = 0
        for x in range(0, len(A)):
            for y in range(1,len(A)):
                if A[y]>A[y-1]:
                    swap+=1
                    A[y],A[y-1]= A[y-1], A[y]
        return swap

s = Solution()
#print(s.sqrt(11))
print(s.solve([5, 3, 1, 9, 4]))