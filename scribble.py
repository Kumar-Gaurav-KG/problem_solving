num = 10
print(bin(num).split('0b')[1])
if num&1==1:
    print("hi")
'''while(num>0):
    num = num>>1
    print(num & 1, end=" ")
    num = num//2'''