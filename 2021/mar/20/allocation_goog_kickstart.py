tes = int(input())
for t in range(tes):
    n, b = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    a.sort()
    co = 0
    for i in a:
        if i <= b:
            co = co+1
            b = b-i
        else:
            break
    print("Case #"+str(t+1) + ":", co)
