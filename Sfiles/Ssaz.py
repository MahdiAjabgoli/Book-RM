import random

filee = 'S1'
hile = ''
s = 1
while True:
    b = open(f'S', 'r').read()
    Q = random.choice(b)
    l = len(hile)

    if l < s:
        hile += Q

    if l > s:
        hile = ''

    if l == s:
        a = open(f'{filee}', 'r')
        r = a.read()
        v = r.find(hile)
        
        if v >= 0:
            hile = ''
        else:
            a = open(f'{filee}', 'a')
            a.write(hile)
            a.write("\n")



input('FINISH')
