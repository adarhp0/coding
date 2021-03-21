tes = int(input())
for t in range(tes):
    n, k = map(int, input().split(' '))
    s = input()
    gp = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            gp = gp+1
            # print(i)
    if gp == k:
        print("Case #"+str(t+1) + ":", 0)
    else:
        print("Case #"+str(t+1) + ":", abs(gp-k))
