tes = int(input())
for t in range(tes):
    k1, k2, k3, v = map(float, input().split())
    f_sp = k1*k2*k3*v
    f_time = round(100/f_sp, 2)
    if f_time < 9.58:
        print("YES")
    else:
        print("NO")
