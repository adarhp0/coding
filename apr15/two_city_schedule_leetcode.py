def twoCitySchedCost(cs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    c = 0
    an = 0
    bn = 0
    n = len(cs)
    m = int(n/2)
    za = []
    zb = []
    visi = []
    for i in range(n):
        za.append((cs[i][0]-cs[i][1], i))
        zb.append((cs[i][1]-cs[i][0], i))
        visi.append(0)
    za.sort()
    zb.sort()
    za = za[::-1]
    zb = zb[::-1]
    i = 0
    j = 0

    while i < n and j < n and an < m and bn < m:
        if za[i][0] > zb[j][0]:
            ind = za[i][1]
            if visi[ind] == 0:
                c = c+cs[ind][1]
                i = i+1
                an = an+1
                visi[ind] = 1
            else:
                i = i+1
        else:
            ind = zb[j][1]
            if visi[ind] == 0:
                c = c+cs[ind][0]
                j = j+1
                bn = bn+1
                visi[ind] = 2
            else:
                j = j+1
    if an != m:
        while i < n and an < m:
            ind = za[i][1]
            if visi[ind] == 0:
                c = c+cs[ind][1]
                i = i+1
                an = an+1
                visi[ind] = 1
            else:
                i = i+1
    if bn != m:
        while j < n and bn < m:
            ind = zb[j][1]
            if visi[ind] == 0:
                c = c+cs[ind][0]
                j = j+1
                bn = bn+1
                visi[ind] = 2
            else:
                j = j+1

        print("ij", an, bn)
        print(visi)
        print("za", za)
        print("zb", zb)
    return c


cs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(twoCitySchedCost(cs))

"""
expe 1859


got 1706
a=770+
b=

"""
