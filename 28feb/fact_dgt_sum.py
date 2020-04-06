global fa
global l
l=[]
fa=[1,1,2,6,24,120,720,5040,40320,362880]
def fact(n):
    fl=0
    if n>0:
        for i in range(10):
            if n<fa[i]:
                l.append(i-1)
                n=n-fa[i-1]
                fl=1
                fact(n)
                break
            elif n==fa[i]:
                l.append(i)
                n=n-fa[i]
                fl=1
                fact(n)
                break
        if fl==0:
            l.append(9)
            n=n-362880
            fact(n)
tes=int(input())
for t in range(tes):
    x=int(input())
    n=x
    fl=0
    if n==0:
        print(-1)
    else:
        while n>0:
            for i in range(10):
                if n<fa[i]:
                    l.append(i-1)
                    n=n-fa[i-1]
                    fl=1
                    fact(n)
                    break
                elif n==fa[i]:
                    l.append(i)
                    n=n-fa[i]
                    fl=1
                    break
            if fl==0:
                l.append(9)
                n=n-362880
                
        n1=len(l)
        for i in range(n1):
            if l[i]==0:
                l[i]=1
        l.sort()
        
        
        for i in range(n1):
            print(l[i],end="")
        print()    
