def findContentChildren(g, s):
    c = 0
    g.sort()
    s.sort()
    gn = len(g)
    sn = len(s)
    # i=0
    # j=0
    for i, j in g, s:
        if i <= j:
            c = c+1
            i = i+1
            j = j+1
        else:
            j = j+1
    return c


findContentChildren([1, 2, 3], [1, 1])
