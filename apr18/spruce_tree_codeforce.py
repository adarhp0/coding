n = int(input())
a = [1]*(n+1)
a[0] = 0
b = [0]*(n+1)
b[0] = -1
b[1] = 1
p = {}
fl = 1
for i in range(2, n+1):
    a[i] = int(input())
    b[a[i]] = 1
    p[a[i]] = []
for i in range(2, n+1):
    p[a[i]].append(i)
c = 0
for keys in p:
    z = p[keys]
    c = 0
    for i in z:
        if b[i] == 0:
            c = c+1
    if c < 3:
        fl = 0
        break
if fl == 0:
    print("No")
else:
    print("Yes")
