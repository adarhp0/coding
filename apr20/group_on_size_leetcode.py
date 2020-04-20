from collections import defaultdict


class Solution(object):
    def groupThePeople(gs):
        a = defaultdict(list)
        b = []
        n = len(gs)
        for i in range(n):
            a[gs[i]].append(i)
        for k in a:
            z = a[k]
            n = len(z)
            m = n // k
            for i in range(m):
                b.append(z[i*k:i*k+k])
        return b


gs = [2, 1, 3, 3, 3, 2]
print(Solution.groupThePeople(gs))
