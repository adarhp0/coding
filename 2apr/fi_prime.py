def pr_chk(a):
    fl=0
    zz=int(a**0.5)
    for i in range(2,zz):
        if a%i==0:
            fl=1
            break
    if fl==1:
        return 1
    else:
        return 0


tes=int(input())
for t in range(tes):
    m,n=map(int,input().split())
    d={}
    for i in range(m,n+1):
        if i%2==0:
            d[i]=1
        else:
            d[i]=0
    a=[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51]
    b=[3,5,7,11,13,17,19,23,29,31,37,39,41,43,47]

    if n>1000000:
        for j in a:
            for i in range(m,n+1):
                if i%j==0:
                    d[i]=1
        for j in b:
            d[i]=0
            
    for i in range(m,n+1):
        if d[i]==0:
            d[i]=pr_chk(i)
    d[2]=0
    d[1]=1
    for i in range(m,n+1):
        if d[i]==0:
            print(i)
    print()