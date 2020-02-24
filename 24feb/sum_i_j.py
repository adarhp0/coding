def fg(z,x):
    if abs(z-x)>1:
        return x-z
    else:
        return 0
tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    z=0
    for i in range(n):
        for j in range(i+1,n):
            z=z+fg(l[i],l[j])
    print(z)