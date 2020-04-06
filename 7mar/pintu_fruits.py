import sys
tes=int(sys.stdin.readline())
for t in range(tes):
    n,m=map(int,input().split())
    fi=list(map(int,input().split()))
    pi=list(map(int,input().split()))
    l=[]
    for i in range(m+1):
        l.append(0)
    for i in range(n):
        f=fi[i]
        p=pi[i]
        l[f]=l[f]+p
    z1=max(l)
    for i in range(m+1):
        if l[i]==0:
            l[i]=z1+1

    print(min(l))