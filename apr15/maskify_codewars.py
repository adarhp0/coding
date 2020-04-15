# return masked string
def maskify(cc):
    a = ''
    if len(cc) <= 4:
        a = cc
        return a
    else:
        n = len(cc)
        for i in range(n-4):
            a = a+'#'
        for i in range(n-4, n,):
            a = a+cc[i]
        return a
    pass
