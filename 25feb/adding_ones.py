tes=int(input())
for t in range(tes):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    a=[]
    for i in range(n+1):
        a.append(k)
    for j in l:
        for i in range(1,n+1):
            if i<j:
                a[i]=a[i]-1
            else:
                break
    for i in range(1,n+1):
        print(a[i],end=" ")
    print()