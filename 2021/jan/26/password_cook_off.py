tes = int(input())
for t in range(tes):
    ps = input()
    fl = 1
    num_fl = 0
    cap_fl = 0
    spl_fl = 0
    lower_fl = 0
    n = len(ps)
    if len(ps) > 9:
        i = 0
        if (ps[0] >= 'A' and ps[0] <= 'Z') or (ps[-1] >= 'A' and ps[-1] <= 'Z'):
            fl = 0
        else:
            while (num_fl == 0 or cap_fl == 0 or lower_fl == 0 or spl_fl == 0) and i < n:
                if ps[i] >= 'a' and ps[i] <= 'z':
                    lower_fl = 1
                elif ps[i] >= 'A' and ps[i] <= 'Z':
                    cap_fl = 1
                elif ps[i] == '@' or ps[i] == '#' or ps[i] == '%' or ps[i] == '&' or ps[i] == '?':
                    spl_fl = 1
                else:
                    num_fl = 1
                i = i+1
    else:
        fl = 0
    if fl == 1 and (num_fl+cap_fl+lower_fl+spl_fl == 4):
        print("YES")
    else:
        print("NO")
