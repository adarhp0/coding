tes=int(input())
for t in range(tes):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    pr=list(map(int,input().split()))
    arr1=arr
    #arr.sort()
    l=[]
    a1=[]
    for i in range(n):
        if arr1[i]!=arr[i]:
            l.append(i)
    if len(l)==-1:
        print("YES")
    else:
        q=len(l)
        ar_inv=[]
        seg_ar=[]
        seg_ar1=[]
        for i in range(n):
            seg_ar.append(-1)
            seg_ar1.append(-1)
        for i in range(n):
            for j in range(i+1,n):
                if arr1[i]>arr1[j]:
                    for k in range(i,j+1):
                        seg_ar[k]=1
        for i in range(m):
            v=pr[i]
            seg_ar1[v]=1
            seg_ar1[v-1]=1
        print(seg_ar,seg_ar1)
        