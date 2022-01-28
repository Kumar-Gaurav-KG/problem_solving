# 5312 -->sum = 11
def reverse_of_no(n):
    rev = ''
    while n>0:
        mod = n%10
        rev +=str(mod)
        n = n//10
    return rev

print(reverse_of_no(12345678910))
