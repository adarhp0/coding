tes = int(input())
for t in range(tes):
    n = int(input())
    l = list(map(int, input().split()))
    a = {}

    for i in l:
        a[i] = a[i]+1
    uniq = 0
    for keys in a:
        if a[keys] == 1:
            uniq = uniq+1
    s2 = max(list(a.values()))
    print(s2)
