tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    a={}
    for i in range(n):
        a[l[i]]=0
    for i in range(n):
        a[l[i]]=a[l[i]]+1
    for keys in a:
        if a[keys]==1:
            print(keys)
            break
    