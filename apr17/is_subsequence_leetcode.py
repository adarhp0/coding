def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    tn = len(t)
    fl = 0
    tj = 0
    for i in s:
        fl = 0
        for j in range(tj, tn):
            if i == t[j]:
                tj = j+1
                fl = 1
                break
        if fl == 0:
            return False
    return True
