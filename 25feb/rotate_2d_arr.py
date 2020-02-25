tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(l[n*i:(i+1)*n])
    for i in range(n):
        for j in range(i,n):
            z=a[i][j]
            a[i][j]=a[j][i]
            a[j][i]=z
    k=[]
    for i in range(n):
        k=a[i]
        k=k[::-1]
        a[i]=k
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=" ")
    print()