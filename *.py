n = input()
k = int(input())
t = 1
s = 0
c = 0
lc = 0
for i in range(k):
    c = s
    c -= lc
    s += int(n) * t + c
    t *= 10
    lc = c
print(s)