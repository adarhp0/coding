class Solution:
    def minNumberOfFrogs(cf):
        c = r = o = a = k = 0
        f = 0
        for ch in cf:
            if ch == 'c':
                c += 1
                f = max(f, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            elif ch == 'k':
                k += 1
            else:
                return -1
            if not c >= r >= o >= a >= k:
                return -1
        return f if c == r == o == a == k else -1


cf = input()
print(Solution.minNumberOfFrogs(cf))
