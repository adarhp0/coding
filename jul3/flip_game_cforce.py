n = int(input())
l = list(map(int, input().split(' ')))
# print(l)
s = 0
sc = 0
e = 0
m_sofar = 0
m_cur = 0
for i in range(n):
    if l[i] == 1:
        m_cur = m_cur-1
    else:
        m_cur = m_cur+1

    if m_cur < 0:
        m_cur = 0
        sc = i+1

    if m_cur > m_sofar:
        m_sofar = m_cur
        s = sc
        e = i

for i in range(s, e+1):
    if l[i] == 1:
        l[i] = 0
    else:
        l[i] = 1
c = 0
for i in range(n):
    if l[i] == 1:
        c = c+1
# print(m_sofar)
#print(s, e)
print(c)
