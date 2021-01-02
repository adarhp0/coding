tes = int(input())
for t in range(tes):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) < k:
        print(0)
    else:
        si = sum(a)
        s1 = si//k
        if s1 >= d:
            print(d)
        else:
            print(s1)
