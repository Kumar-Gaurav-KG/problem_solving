'''
Problem Description

You have an array A with N elements. We have 2 types of operation available on this array :
We can split a element B into 2 elements C and D such that B = C + D.
We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P and Q.
You have to determine whether it is possible to make array A containing only 1 element i.e. 0 after several splits and/or merge?



Problem Constraints

1 <= N <= 100000

1 <= A[i] <= 106



Input Format

The first argument is an integer array A of size N.



Output Format

Return "Yes" if it is possible otherwise return "No".



Example Input

Input 1:

 A = [9, 17]
Input 2:

 A = [1]


Example Output

Output 1:

 Yes
Output 2:

 No


Example Explanation

Explanation 1:

 Following is one possible sequence of operations -  
 1) Merge i.e 9 XOR 17 = 24  
 2) Split 24 into two parts each of size 12  
 3) Merge i.e 12 XOR 12 = 0  
 As there is only 1 element i.e 0. So it is possible.
Explanation 2:

 There is no possible way to make it 0.'''

def solve(A):
    # if no is even, we can split it into two: ex 24 - 12 and 12, 12 xor 12 = 0
    # if no is odd, 9 = 1+8, 8 can be reduced to 0 by dividing into two half, so we can reduce it to 1
    # if two odd then we can reduce it to 1, ex: 1xor1 = 0
    # find no of odd elements in array, if even we can reduce it to 0
    # if no of odd elements in an array is even - we can reduce it to 0
    # else it can be reduced to 1 only
    # even no can be reduced to 0

    count = 0
    for x in A:
        if x&1==1:
            count+=1
    if count&1==0:
        return "Yes"
    else:
        return "No"

print(solve([9, 17]))