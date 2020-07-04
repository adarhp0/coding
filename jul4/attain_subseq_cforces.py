tes = int(input())
for t in range(tes):
    n = int(input())
    l = list(map(int, input().split(' ')))
    a = []
    for i in range(n):
        a.append(0)
    sc = 0

    cr_sgn = ''
    if len(l) > 1:
        if l[0] > 0:
            if l[1] > 0:
                a[0] = 1
                sc = 1
            else:
                a[0] = 0
        else:
            if l[1] < 0:
                a[0] = -1
                sc = 1
            else:
                a[0] = 0
    for i in range(1, n-1):
        pr = l[i-1]
        cr = l[i]
        nx = l[i+1]
        if cr > 0:
            if pr < 0:
                sc = 0
            if nx > 0 or pr > 0:
                sc = sc+1
                a[i] = sc
            else:
                sc = 0
        else:
            if pr > 0:
                sc = 0
            if nx < 0 or pr < 0:
                sc = sc+1
                a[i] = -1*sc
            else:
                sc = 0
    if len(l) > 1:
        if l[n-1] > 0:
            if l[n-2] > 0:
                a[n-1] = abs(a[n-2])+1
            else:
                a[n-1] = 0
        else:
            if l[n-2] < 0:
                a[n-1] = -1*(abs(a[n-2])+1)
                sc = 1
            else:
                a[n-1] = 0
    else:
        c = max(l)

    i = 0
    st = '*'
    z = []
    c = 0
    while i < n:
        if a[i] == 0:
            if st == '*':
                c = c+l[i]
                #print("neutral", l[i])
            elif st != '*':
                c = c+max(z)
                c = c+l[i]
                #print("neutral", l[i])
                st = '*'

            z = []
            i = i+1
        elif a[i] > 0:
            if st == '*' or st == '+':
                st = '+'
                z.append(l[i])
                i = i+1
            elif st == '-':
                c = c+max(z)
                #print("neg", z)
                z = []
                z.append(l[i])
                i = i+1
                st = '+'
        elif a[i] < 0:
            if st == '*' or st == '-':
                st = '-'
                z.append(l[i])
                i = i+1
            elif st == '+':
                c = c+max(z)
                #print("pos", z)
                z = []
                z.append(l[i])
                i = i+1
                st = '-'
    if st != '*':
        if len(z) > 0 and z[0] > 0:
            c = c+max(z)
            #print("pos", z)
        elif len(z) > 0 and z[0] < 0:
            c = c+max(z)
            #print("neg", z)

    print(c)
