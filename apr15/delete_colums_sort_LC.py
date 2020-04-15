def lastStoneWeight(self, s):
    n = len(s)
    s.sort()
    while n > 1:
        x = s.pop()
        # print(s)
        y = s.pop()
        n = n-2
        if abs(x-y) != 0:
            s.append(abs(x-y))
            n = n+1
        elif n == 0:
            return 0
        s.sort()
        # print(s)

    return s[0]
