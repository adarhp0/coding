tes = int(input())
for t in range(tes):
    n = int(input())
    cou = 0
    for i in range(1, n+1):
        x = str(i)
        if x.__contains__('4'):
            cou = cou+1
    print(cou)
