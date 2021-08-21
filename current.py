st = '/home/user/Документы/text.txt'
stroki = 8
t = open(st)
d = {}
for i in range(stroki):
    i = t.readline()[:-1].split(' : ')
    if i == ['']:
        pass
    else:
        d[i[0]] = i[1]
print(d)