def in_array(array1, array2):
    # your code
    s = ''
    a = []
    for i in array2:
        s = s+i
    for i in array1:
        if s.__contains__(i):
            a.append(i)
    # a1=set(a)
    a2 = list(set(a))
    a2.sort()
    return a2
