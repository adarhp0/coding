tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    ls=set(l)
    ll=list(ls)
    #print(ls)
    #print(ll)
    nl=len(ll)
    a={}
    b={}
    for i in range(nl):
        a[ll[i]]=[]
        b[ll[i]]=-1
    for i in range(n):
        a[l[i]].append(i)
    for i in range(nl):
        k=a[ll[i]]
        try:
            b[ll[i]]=k[-1]-k[0]
        except:
            b[ll[i]]=0
    #print(a)
    bl=list(b.values())
    print(max(bl))