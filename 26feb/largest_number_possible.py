tes=int(input())
for t in range(tes):
    n,s=map(int,input().split())
    if s/n>9 or s==0:
        print(-1)
    else:
        z={}
        for i in range(10):
            z[i]=0
        q=9
        while s>0:
            z[q]=int(s/q)
            s=s-z[q]*q
            q=q-1
        a=''
        su=0
        for i in range(9,0,-1):
            k=z[i]
            su=su+k
            for j in range(k):
                a=a+str(i)
        b=n-su
        for i in range(b):
            a=a+str(0)
        print(a)
        #print(z)


