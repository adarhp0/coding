def balancedStringSplit(self, s):
    """
    :type s: str
    :rtype: int
    """
    l=len(s)
    co=0
    rc=0
    lc=0
    b=''
    for i in range(l):
        if s[i]=='R':
            rc=rc+1
        else:
            lc=lc+1
        b=b+s[i]
        if rc==lc and rc !=0 and lc!=0:
            co=co+1
            b=''
            rc=0
            lc=0
    return co
s=input()
balancedStringSplit(s)