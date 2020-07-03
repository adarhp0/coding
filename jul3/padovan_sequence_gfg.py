def padovan(n):
    # n=(n-2)+(n-3)
    p0 = p1 = p2 = 1
    if n <= 2:
        return 1
    else:
        pn1 = p2
        pn2 = p1
        pn3 = p0
        i = 3
        pn = 0
        while i <= n:
            pn = pn2+pn3
            i = i+1
            pn3 = pn2
            pn2 = pn1
            pn1 = pn
        pn = pn % 1000000007
        return pn


tes = int(input())
for t in range(tes):
    n = int(input())
    print(padovan(n))
