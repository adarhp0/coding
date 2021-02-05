def time_score(ctime):
    chef_am_pm = 0
    if ctime[6] == "A":
        chef_am_pm = 0
    else:
        chef_am_pm = 12*60
    chef_hh = int(ctime[:2]) % 12
    chef_mm = int(ctime[3:5])
    chef_score = chef_am_pm+(chef_hh*60)+chef_mm
    return chef_score


tes = int(input())
for t in range(tes):
    chef_time = input()
    fn = int(input())
    chef_score = time_score(chef_time)
    for f in range(fn):
        fr_time = input()
        fr_time_lower = fr_time[:7]
        fr_time_upper = fr_time[9:]
        fr_l_score = time_score(fr_time_lower)
        fr_u_score = time_score(fr_time_upper)
        if fr_l_score <= chef_score <= fr_u_score:
            print("1", end="")
        else:
            print("0", end="")
    print()
