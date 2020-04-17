n = int(input())
s = input()
n1 = 0
n0 = 0
for i in s:
    if i == '1':
        n1 = n1+1
    else:
        n0 = n0+1
print(abs(n1-n0))
