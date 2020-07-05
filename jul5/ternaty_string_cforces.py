def fi(s, a, c1, c2):
    sr = s[::-1]
    fc1 = fc2 = bc1 = bc2 = -1
    fc1 = s.find(c1)
    fc2 = s.find(c2)
    bc1 = sr.find(c1)
    bc2 = sr.find(c2)
    # print(s)
    if fc1 > fc2:
        f = fc1+1
    else:
        f = fc2+1
    if bc1 > bc2:
        b = bc1+1
    else:
        b = bc2+1
    if f > b:
        return b+1
    else:
        return f+1


def ff(s, a, c1, c2):
    fc1 = fc2 = -1
    fc1 = s.find(c1)
    fc2 = s.find(c2)
    if fc1 > fc2:
        f = fc1+1
    else:
        f = fc2+1
    return f


def sf(s, a, c1, c2):
    sr = s[::-1]
    fc1 = fc2 = -1
    fc1 = s.find(c1)
    fc2 = s.find(c2)
    if fc1 > fc2:
        f = fc1+1
    else:
        f = fc2+1
    return f


tes = int(input())
for t in range(tes):
    s = input()
    n = len(s)
    if (s.__contains__('1')) and (s.__contains__('2')) and (s.__contains__('3')):
        a = {}
        a['1'] = a['2'] = a['3'] = 0
        for i in range(n):
            a[s[i]] = a[s[i]]+1
        i = 0
        j = n-1
        while j-i > 1:
            fp = s[i]
            bp = s[j]
            if a[fp] == 1 and a[bp] == 1:
                print(j+1-i)
                break
            elif a[fp] == 1:
                if fp == '1':
                    print(ff(s[i+1:j+1], a, '2', '3'))
                    break
                elif fp == '2':
                    print(ff(s[i+1:j+1], a, '1', '3'))
                    break
                else:
                    print(ff(s[i+1:j+1], a, '1', '2'))
                    break
            elif a[bp] == 1:
                if fp == '1':
                    print(ff(s[i:j], a, '2', '3'))
                    break
                elif fp == '2':
                    print(ff(s[i:j], a, '1', '3'))
                    break
                else:
                    print(ff(s[i:j], a, '1', '2'))
                    break
            else:
                if a[fp] > a[bp]:
                    a[fp] = a[fp]-1
                    i = i+1
                elif a[bp] > a[fp]:
                    a[bp] = a[bp]-1
                    j = j-1
                elif a[fp] == a[bp] and fp == bp and a[fp] == 2:
                    # complicated need to find where the nxt other 2 lies then based on that work on it
                    if fp == '1':
                        print(fi(s[i+1:j], a, '2', '3'))
                        break
                    elif fp == '2':
                        print(fi(s[i+1:j], a, '1', '3'))
                        break
                    elif fp == '3':
                        print(fi(s[i+1:j], a, '2', '1'))
                        break
                else:
                    a[fp] = a[fp]-1
                    a[bp] = a[bp]-1
                    i = i+1
                    j = j-1

    else:
        print(0)
