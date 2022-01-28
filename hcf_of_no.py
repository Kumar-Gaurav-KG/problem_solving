def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())

    for _ in range(n):
        i,j = map(int, input().split(" "))
        #print(i,j)
        hcf = 1
        if i==0 or j==0:
            hcf = max(i,j)
        for x in range(1,min(i,j)+1):
            #print(x)
            if i%x==0 and j%x==0:
                hcf = x

        print(hcf)
    return 0

if __name__ == '__main__':
    main()