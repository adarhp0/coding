tes=int(input())
for t in range(tes):
    n=int(input())
    l1=list(map(int,input().split()))
    k=int(input())
    c=0
    for i in range(n): 
        min_idx = i
        c=c+1
        for j in range(i+1, n): 
            if l1[min_idx] >l1[j]: 
                min_idx = j 
        l1[i], l1[min_idx] = l1[min_idx], l1[i]
        if c==k:
            print(l1[k])
            break
