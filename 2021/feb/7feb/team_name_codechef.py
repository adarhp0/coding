from collections import defaultdict


def def_value():
    return set()


tes = int(input())
for t in range(tes):
    n = int(input())
    na_l = input()
    l1 = na_l.split(" ")
    fir_lset = set()
    ald = defaultdict(def_value)
    sec_lset = set()
    for i in l1:
        ald[i[0]].add(i[1:])
        fir_lset.add(i[0])
        sec_lset.add(i[0])
    ll = list(fir_lset)
    n1 = len(ll)
    co = 0
    l_s = set(l1)

    for i in fir_lset:
        sec_lset.discard(i)
        wl1 = ald[i]
        for j in sec_lset:
            wl2 = ald[j]
            s1 = wl1-wl2
            s2 = wl2-wl1
            for k1 in s1:
                r1 = j+k1
                for k2 in s2:
                    r2 = i+k2
                    if r1 not in l_s and r2 not in l_s:
                        co = co+1
    print(co*2)

    """
    co = 0
    l_s = set(l1)
    for i in range(n):
        w1 = l1[i]
        for j in range(i+1, n):
            w2 = l1[j]
            r1 = w2[0]+w1[1:]
            r2 = w1[0]+w2[1:]
            # print(r1, r2)
            if w1[0] == w2[0] or w1[1:] == w2[1:]:
                z = 1
            elif r1 not in l_s and r2 not in l_s:
                # print(w1, w2)
                co = co+1
    print(co*2)
    """
