def sum(n):
    sum=0
    while (n>0 or sum>9):
        if (n==0):
            n=sum;
            sum=0
        sum += n % 10
        n /= 10
    return  sum




for _ in range(int(input())):
    n = int(input())

    if sum(n)==1:
        print("1")
    else :
        print("0")


    if __name__ == '__main__':
        pass
