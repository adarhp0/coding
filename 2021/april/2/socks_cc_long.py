a, b, c = map(int, input().split())
fl = 0
if a == b or a == c:
    fl = 1
elif b == c:
    fl = 1
if fl == 1:
    print("YES")
else:
    print("NO")
