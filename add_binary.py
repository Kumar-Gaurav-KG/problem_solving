def add_binary(A,B):
    res = ""
    print(min(len(A), len(B)))
    carry = 0
    for i in range(min(len(A), len(B))-1,-1,-1):
        print("-"*50)
        print(i)
        print(int(A[i]), int(B[i]))
        s = int(A[i])+int(B[i]) + carry
        print(f"s:{s}")
        summ = s%2
        print(f"sum:{summ}")
        res+=str(summ)
        print(f"result: {res}")
        carry = summ//2
        print(f"carry: {carry}")
        print("-"*50)
    print(res)



add_binary("100","11")