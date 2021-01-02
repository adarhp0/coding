di = {}
di['0000'] = 'a'
di['0001'] = 'b'
di['0010'] = 'c'
di['0011'] = 'd'
di['0100'] = 'e'
di['0101'] = 'f'
di['0110'] = 'g'
di['0111'] = 'h'
di['1000'] = 'i'
di['1001'] = 'j'
di['1010'] = 'k'
di['1011'] = 'l'
di['1100'] = 'm'
di['1101'] = 'n'
di['1110'] = 'o'
di['1111'] = 'p'
tes = int(input())
for t in range(tes):
    n = int(input())
    s = input()
    n1 = n//4
    z = ''
    for i in range(n1):
        k = s[i*4:(i*4)+4]
        z = z+di[k]
    print(z)
