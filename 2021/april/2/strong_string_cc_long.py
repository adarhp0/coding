tes = int(input())
for t in range(tes):
    n, k = map(int, input().split())
    s = input()
    z = s.count('*')
    if z < k:
        print("NO")
    else:
        co = 0
        fl = 0
        ff = 0
        for i in s:
            if i == '*' and fl == 1:
                co = co+1
            elif i == '*' and fl == 0:
                fl = 1
                co = co+1
            elif i != '*' and fl == 1:
                fl = 0
                co = 0
            if co >= k:
                ff = 1
                break
        if ff == 1:
            print("YES")
        else:
            print("NO")
