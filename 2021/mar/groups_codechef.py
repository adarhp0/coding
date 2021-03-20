tes = int(input())
for t in range(tes):
    s = input()
    gr_n = 0
    z_fl = False
    o_fl = False
    n = len(s)
    if s[0] == '0':
        z_fl = True
    else:
        o_fl = True
        gr_n = gr_n+1
    for i in range(1, n):
        if z_fl == True and s[i] == '1':
            gr_n = gr_n+1
            z_fl = False
            o_fl = True
        elif o_fl == True and s[i] == '1':
            z_fl = False
        elif o_fl == True and s[i] == '0':
            z_fl = True
            o_fl = False
    print(gr_n)
