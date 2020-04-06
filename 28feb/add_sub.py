tes=int(input())
for t in range(tes):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif b>a:
        z=b-a
        if z%2==0:
            print(2)
        else:
            print(1)
    else:
        z=a-b
        if z%2==0:
            print(1)
        else:
            print(2)
    
