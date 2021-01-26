tes = int(input())
for t in range(tes):
    n, k, x, y = map(int, input().split())
    corner_hit = 0
    lx = -1
    ly = -1
    if x == y:
        corner_hit = 1
        lx = n
        ly = n
    else:
        # for 1st quadrant
        x1, y1 = x, y
        while x1 != n and y1 != n:
            x1 = x1+1
            y1 = y1+1
        # for 2nd quadrant
        x2, y2 = x1, y1
        x2 = x2-1
        y2 = y2+1
        while x2 != n and y2 != n:
            x2 = x2-1
            y2 = y2-1
        # for 3rd quadrant
        x3, y3 = x2, y2
        x3 = x3-1
        y3 = y3-1
        while x3 !=
