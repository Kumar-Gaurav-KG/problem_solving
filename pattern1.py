'''
    1
   232
  34543
 4567654
567898765

'''

# 1) each row starts with row number
# 2) N rows
# 3) spaces = N-i
# 4) each row has i increasing number and i-1 decreasing number
n = 5
i = 1
while i<=n:
    print(" "*(n-i),end='')
    p = i
    k = 1
    while k<=i:
        print(str(p), end='')
        k+=1
        p+=1
    j =1
    p-=1
    while j <= i-1:
        print(str(p-1), end='')
        p-=1
        j+=1 
    print("\n")
    i +=1


