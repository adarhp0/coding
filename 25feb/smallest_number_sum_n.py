def fn(s):
    a1=str(s)
    al=list(a1)
    z=0
    for i in al:
        z=z+int(i)
    return z
tes=int(input())
for t in range(tes):
    n=int(input())
    an=10**n
    f1=1
    ab=10**n
    i=2
    #print(an)
    if n>9:
        r=n%9
        q=int(n/9)
        s=''
        if r!=0:
            s=s+str(r)
        for i in range(q):
            s=s+'9'
        for i in range(n):
            s=s+'0'
        print(s)
    else:
        while f1:
            kk=fn(ab)
            if kk==n:
                print(ab)
                break
            else:
                #print(ab)
                ab=an*i
                i=i+1