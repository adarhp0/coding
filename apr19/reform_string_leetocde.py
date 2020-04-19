def reformat(self, sa):
    """
    :type s: str
    :rtype: str
    """
    s = list(sa)
    nn = 0
    na = 0
    la = []
    ln = []
    for i in s:
        # print(str(i))
        if ord(str(i)) > 96 and ord(str(i)) < 123:
            na = na+1
            la.append(str(i))
        else:
            nn = nn+1
            ln.append(str(i))
    i = 0
    j = 0
    z = ''
    if na > nn:
        while i < na and j < nn:
            z = z+la[i]
            z = z+ln[j]
            i = i+1
            j = j+1
        z = z+la[i]
        if len(z) != (nn+na):
            return ""
        else:
            return z
    else:
        while i < na and j < nn:
            z = z+ln[j]
            z = z+la[i]
            i = i+1
            j = j+1
        if na < nn:
            z = z+ln[j]
        if len(z) != (nn+na):
            return ""
        else:
            return z
