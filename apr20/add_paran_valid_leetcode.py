class Solution(object):
    def minAddToMakeValid(s):
        l = r = 0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1

        return l+r


s = input()
print(Solution.minAddToMakeValid(s))
