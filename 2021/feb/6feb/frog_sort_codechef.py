import math
tes = int(input())
for t in range(tes):
    n = int(input())
    wpdic = {}
    ldic = {}
    temp1 = list(map(int, input().split()))
    temp2 = list(map(int, input().split()))
    for i in range(n):
        wpdic[temp1[i]] = i+1
        ldic[temp1[i]] = temp2[i]
    # print(wpdic)
    # print(ldic)
    temp1.sort()
    t_hit = 0
    # print(temp1)
    for i in range(n-1):
        pos_0 = wpdic[temp1[i]]
        pos_1 = wpdic[temp1[i+1]]
        wt_0 = temp1[i]
        wt_1 = temp2[i+1]
        l_0 = ldic[temp1[i]]
        l_1 = ldic[temp1[i+1]]
        if pos_0 > pos_1:
            #print("i", temp1[i])
            while wpdic[temp1[i+1]] <= wpdic[temp1[i]]:
                #print("chg wt", wpdic[temp1[i+1]])
                wpdic[temp1[i+1]] = wpdic[temp1[i+1]]+l_1
                t_hit = t_hit+1
        elif pos_1 == pos_0 and wt_0 != wt_1:
            #print("i1", temp1[i])
            t_hit = t_hit+1
            wpdic[temp1[i+1]] = wpdic[temp1[i+1]]+l_1
    print(t_hit)
