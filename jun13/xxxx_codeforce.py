def subarr(a, n, x):
    s1 = sum(a)
    if s1 % x != 0:
        return n
    f1 = 0
    for i in a:
        if i % x == 0:
            f1 = f1+1
    if f1 == n:
        return 0

    m_so_far = 0
    m_end_here = 0
    z = set()
    for i in range(n):
        m_end_here = m_end_here+a[i]
        if m_end_here < 0:
            m_end_here = 0
        elif m_end_here > m_so_far:
            m_so_far = m_end_here
        z.add(m_so_far)
    return list(z)


tes = int(input())
for t in range(tes):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(subarr(a, n, x))
