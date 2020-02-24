tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    ls=set(l)
    ll=list(ls)
    nl=len(ll)
    m2=max(ll)
    m1=min(ll)
    a={}
    for i in range(m1,m2+1):
        a[i]=0
    z=0
    for i in range(n):
        a[l[i]]=a[l[i]]+1
    for i in range(m1,m2):
        z=z+((n-a[i])*a[i])
        n=n-a[i]
    print(z)