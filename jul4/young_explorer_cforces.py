tes = int(input())
for t in range(tes):
    n = int(input())
    l = list(map(int, input().split(' ')))
    l.sort()
    co = 0
    acti = 0
    bn = 0
    i = 0
    while i < n:
        z = l[i]
        bn = bn+1
        i = i+1
        if bn == z:
            co = co+1
            bn = 0
    print(co)
