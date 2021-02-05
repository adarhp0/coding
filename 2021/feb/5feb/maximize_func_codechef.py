tes = int(input())
for t in range(tes):
    n = int(input())
    l1 = list(map(int, input().split()))
    a = max(l1)
    c = min(l1)
    print(2*(a-c))
