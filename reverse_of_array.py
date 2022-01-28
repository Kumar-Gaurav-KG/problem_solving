def solve(A, B):
    print(A)
    result = []

    def reverse(ar, start, end):
        while(start<end):
            ar[start], ar[end] = ar[end], ar[start]
            start+=1
            end-=1
        return ar


    
    for x in B:
        if x%len(A)==0:
            print(A)
            break
        else:
            x = x%len(A)
            ar = reverse(A.copy(), 0, len(A)-1)
            print(A, ar)
            ar = reverse(ar, 0, len(ar)-x-1)
            print(ar)
            ar = reverse(ar, len(ar)-x, len(ar)-1)
            print(ar)



solve([1,2,3,4,5], [2,3,7])