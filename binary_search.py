import math

print(math.ceil(1.7))

def binary_search(n, num):
    lenth = len(n) # 5
    divide = math.floor(lenth/2) # 1 
    print(lenth, divide, n)
    if n[divide] == num:
        return n[divide], divide
    else:
        if n[divide]>num:
            return binary_search(n[:divide], num)
        else:
            return binary_search(n[divide:],num) 
        
n, ind = binary_search([1,4,5,9,10], 5)
print(n, ind)