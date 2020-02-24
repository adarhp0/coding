tes=int(input())
for t in range(tes):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    x1,y1,x2,y2=map(int,input().split())
    z=0
    for i in range(n):
        c=[]
        for j in range(z,z+m):
            c.append(a[j])
        z=z+m
        b.append(c)
    z=0
    #print(b)
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            z=z+b[i][j]
    print(z)
    '''
    for i in range(x1-1,x2):
        z=z+sum(b[i])
        #print(b[i])
    for i in range(y1-1):
        z=z-b[x1-1][i]
        #print(b[x1-1][i],end=" ")
    print("yell")
    for i in range(y2,m):
        z=z-b[x2-1][i]
        #print(b[x2-1][i])
        '''