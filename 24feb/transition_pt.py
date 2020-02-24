tes=int(input())
for t in range(tes):
    n=int(input())
    arr=list(map(int,input().split()))
    fl=0
    j=-1
    for i in range(n):
        if arr[i]==1:
            fl=1
            j=i
            break
    print(j)