tes = int(input())
for t in range(tes):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    h = h[::-1]
    t1 = h[0]
    t2 = 0
    j = 0
    f1 = 0
    for i in range(1, n):
        #print("i", i)
        if t1+h[i] < k and t2+h[i] < k:
            if t1 > t2:
                t2 = t2+h[i]
            else:
                t1 = t1+h[i]
        elif t1+h[i] > k and t2+h[i] > k:
            if t1 > t2:
                t2 = t2+h[i]
            else:
                t1 = t1+h[i]
        elif t1+h[i] <= k:
            t1 = t1+h[i]
            # a1.append(h[i])
        elif t2 >= k:
            t1 = t1+h[i]
            # a1.append(h[i])
        else:
            t2 = t2+h[i]
            # a2.append(h[i])
        if t1 >= k and t2 >= k:
            f1 = 1
            j = i+1
            #print(t1, t2)
            break
    if f1 == 1:
        print(j)
    else:
        print(-1)
    # print(a1)
    # print(a2)
