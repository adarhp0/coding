'''https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0'''

tes=int(input())
for t in range(tes):
    n,d=map(int,input().split())
    ll=list(map(int,input().split()))
    d=d%n
    l1=[]
    l1=ll[d:]
    l1.extend(ll[:d])
    for i in range(n):
        print(l1[i],end=" ")
    print()