st = 'pythonist'
l = [i for i in st]
d = {}
l.sort()
s = set()
lc = l[0]
c = 1
for i in l:
    if i == lc:
        if i == l[0]:
            d[lc] = c
            c = 1
        else:
            c += 1
    else:
        d[lc] = c
        c = 1
    lc = i

print(d)
