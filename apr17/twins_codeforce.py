n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)
u = 0
c = 0
for i in a:
    u = u+i
    c = c+1
    s = s-i
    if u > s:
        break
print(c)
