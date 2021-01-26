tes = int(input())
for t in range(tes):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    na = len(a)
    nb = len(b)
    if sum(a) > sum(b):
        print(0)
    else:
        a.sort()
        b.sort()
        b = b[::-1]
        sw = 0
        ia = 0
        ib = 0
        fl = 0
        while sw < na:
            a[ia], b[ib] = b[ib], a[ia]
            ia = ia+1
            ib = ib+1
            sw = sw+1
            if sum(a) > sum(b):
                fl = 1
                break
        if fl == 0:
            print(-1)
        else:
            print(sw)
