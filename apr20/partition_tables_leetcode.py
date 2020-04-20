from collections import defaultdict


class Solution(object):
    def partitionLabels(s):
        a = defaultdict(int)
        for i in s:
            a[i] += 1
        b = []
        sa = ''
        for i in s:
            sa += i
            # print(sa)
            a[i] -= 1
            k = 0
            sb = set(sa)
            for j in sb:
                if a[j] != 0:
                    k = 1
                    break
                else:
                    k = 0
            # print(sa)
            if k == 0:
                b.append(len(sa))
                sa = ''
        return b


s = input()
print(Solution.partitionLabels(s))
