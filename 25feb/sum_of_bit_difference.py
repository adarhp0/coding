tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    z=0
    for i in range(n):
        for j in range(i+1,n):
            c=bin(l[i]^l[j])
            z=z+2*(c.count('1'))
    print(z)
