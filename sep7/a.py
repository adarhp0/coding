import sys
tes = int(sys.stdin.readline())
for t in range(tes):
    n1 = input()
    z = input()
    l = list(map(int, z.split(" ")))
    # meet time list
    n = int(n1)
    sl = [[-1]*n]*n
    a = []
    # final list
    fl = []
    for i in range(n):
        fl.append([])
    # l.insert(0, -1)
    for i in range(n):
        a.append(-1)
    # for i in range(n):

    # find can if they meet and update it
    # sl[1][2] = 1
    # sl[2][1] = 1
    for i in range(n):
        for j in range(n):
            if(i != j):
                print(i, j, sl)
                t1 = (j-i)//(l[i]-l[j])
                tmod = (j-i) % (l[i]-l[j])
                if tmod == 0 and t1 > 0:
                    if isinstance(t1, int):
                        sl[i][j] = t1
                        sl[j][i] = t1
                        fl[i].append(j)
                        fl[j].append(i)
            else:
                sl[i][j] = -1
    for i in range(n):
        inf = len(fl[i])
        if inf > 0:
            for j in range(len(fl[i])):
                mem = fl[i][j]
                mem_time = sl[i][mem]
                for k in range(n):
                    if sl[mem][k] >= mem_time and k != i:
                        fl[i].append(k)
    print(sl)
    print(l)
    for i in range(n):
        fl[i].append(i)
    print(fl)
