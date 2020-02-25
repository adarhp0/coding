tes=int(input())
for t in range(tes):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(n):
        print(l[i],end=" ")
    print()
