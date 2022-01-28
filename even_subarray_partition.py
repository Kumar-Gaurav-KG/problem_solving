'''
You are given an integer array A.

Decide whether it is possible to divide the array into one or more subarrays of even length such that first and last element of all subarrays will be even.

Return "YES" if it is possible otherwise return "NO" (without quotes).
Example Input
Input 1:

 A = [2, 4, 8, 6]
Input 2:

 A = [2, 4, 8, 7, 6]


Example Output
Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation
Explanation 1:

 We can divide A into [2, 4] and [8, 6].
Explanation 2:

 There is no way to divide the array into even length subarrays.'''

def solve(A):
    l = -1
    if A[0]%2!=0 or A[len(A)-1]%2!=0:
        return "NO"
    else:
        i=0
        while i<len(A):
            if A[i]%2==0:
                if i==len(A)-1:
                    return "NO"
                for j in range(i+1, len(A)):
                    if A[j]%2==0:
                        l = (j-i+1)
                        if l==1:
                            continue
                        print(l)
                        print(A[i:j+1])
                        if l%2!=0:
                            continue
                        else:
                            try:
                                if A[j+1]%2!=0:
                                    continue
                            except:
                                pass
                            i=j+1
                            break
            else:
                return "NO"
                    
                            
                    

    if l%2==0:
        return "YES"
    else:
        return "NO"

print(solve([ 830, 333, 694, 76, 547, 306, 895, 25, 404, 34, 545, 801, 608, 63, 521, 23, 352, 425, 433, 373, 73, 541, 943, 685, 537, 339, 438, 866, 714, 634, 760, 564, 110, 513, 312, 329, 318, 436, 421, 924, 379, 338, 228, 43, 278, 436, 69, 988, 450, 638, 276, 510, 393, 376, 566, 304, 850, 58, 640, 570, 565, 461, 468, 441, 27, 850, 465, 186, 71, 417, 732, 366, 640, 789, 259, 970, 884, 93, 781, 893, 638 ]))