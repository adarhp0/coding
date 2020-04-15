def square_digits(num):
    a = []
    #print(num / 10)
    while num > 0:
        n1 = num % 10
        a.append(n1*n1)
        num = int(num/10)
        # print(num)
    a = a[::-1]
    s = ''
    # print(a)
    for i in a:
        s = s+str(i)
    return int(s)
