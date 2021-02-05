n = int(input())
fl = 0
for i in range(10, 1, -1):
    if n % i == 0:
        print(i)
        fl = 1
        break
if fl == 0:
    print(1)
