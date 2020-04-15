def maxProfit(self, p):
    """
    :type prices: List[int]
    :rtype: int
    """
    f_buy = 0
    i_buy = 0
    a = 0
    n = len(p)
    for i in range(n-1):
        cp = p[i]
        np = p[i+1]
        if f_buy == 0 and cp < np:
            f_buy = 1
            i_buy = i
            # print(i_buy)
        else:
            if cp > np and cp > p[i_buy] and f_buy == 1:
                a = a+cp-p[i_buy]
                # print("sell",cp,np)
                f_buy = 0
    if f_buy == 1:
        a = a+p[-1]-p[i_buy]
    return a
