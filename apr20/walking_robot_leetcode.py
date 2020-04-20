class Solution(object):
    def robotSim(co, ob):
        x = y = p = md = 0
        pr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ob = set(map(tuple, ob))
        for i in co:
            if i == -1:
                p = (p+1) % 4
            elif i == -2:
                p = (p-1) % 4
            else:
                x_off, y_off = pr[p]
                while i:
                    if (x+x_off, y+y_off) not in ob:
                        x += x_off
                        y += y_off
                        i -= 1
                    else:
                        break
                md = max(md, x**2+y**2)
        return md
