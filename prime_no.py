p = int(input())

i =2
c = 0
print(i*i)
while(i*i<p):
    if p%i == 0:
        c =1
        print("NO")
        break
    i+=1
if c == 0:
    print("YES")