tes=int(input())
for t in range(tes):
    n=int(input())
    l=list(map(int,input().split()))
    z=[]
    for i in range(0,n):
        a1=l[2*i]
        a2=l[2*i+1]
        z.append(a1*12+a2)
        if 2*i>= n:
            break
    print(max(z))