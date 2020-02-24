tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    ls=set(l)
    ll=list(ls)
    nl=len(ll)
    a={}
    for i in range(nl):
        a[ll[i]]=0
    for i in range(n):
        a[l[i]]=a[l[i]]+1
    z=0
    al=list(a.values())
    for i in range(nl):
        if al[i]>1:
            z=z+((al[i]*(al[i]-1)))/2
    print(int(z))