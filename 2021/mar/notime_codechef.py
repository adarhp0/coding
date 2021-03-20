n, h, x = map(int, input().split())
l1 = list(map(int, input().split()))
fl = 0
for i in l1:
    if x+i >= h:
        fl = 1
        break
if fl:
    print("YES")
else:
    print("NO")
