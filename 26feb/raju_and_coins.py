import heapq as hq
tes=int(input())
for t in range(tes):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    l.append(1000000001)
    l.append(0)
    c=0
    hq.heapify(l)
    n1=n
    fl=1
    while s>0:
        i=hq.heappop(l)
        j=l[0]
        #print("i j",i,j)
        #print("hello",list(l))
        n1=n1-1
        for k in range(i+1,j):
            if k<=s:
                s=s-k
                c=c+1
                #print(k)
            else:
                fl=0
                break
        if fl==0:
            break
    print(c)

