'''
  *    i=1  stars=1  this is an AP with d=3-1, d= 2
 ***   i=2, stars=3  general equation an= a+(n-1)d = 1+2(n-i) = 1+2n-2 = 2n-1
*****  i=3, stars=5
'''

# pattern
# 1) spaces N-i
# 2) so to find any term we can use 2n-1, so loop will run till 2n-1 for each term
def half_diamond(n):
  i = 1
  while i<=n:
    print(" "*(n-i),end='')
    cnt = 1
    while cnt<=(2*i-1):
      print('*', end="")
      cnt+=1
    print("\n")
    
    i+=1

'''
  *
 ***
*****
 ***
  *
'''
# pattern
#  1 3 5 3 1 - input should be odd. find n/2 +1 = mid 
# till mid starts are in increasing AP, after mid starts are in decreasing


def full_diamond(n):
  i = 1
  sp = 1
  mid = (n//2)
  while i<=n:
    cnt = 1
    if i <= (n//2)+1:
      print(" "*((n//2)+1-i),end='')
      while cnt<=(2*i-1):
        print('*', end="")
        cnt+=1
        #print(1/0)
    else:
      print(" "*(sp),end='')
      cnt = 1
      while cnt <=(2*mid-1):
        print("*", end="")
        cnt +=1
      mid -=1

      sp+=1

    print("\n")
    
    i+=1
                       
full_diamond(9)