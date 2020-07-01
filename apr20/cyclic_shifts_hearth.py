tes = int(input())
for t in range(tes):
    l = list(input().split())
    s = int(l[0])
    s = bin(s).replace("0b", "")
    z = len(l[0])*4
    sl = len(s)
