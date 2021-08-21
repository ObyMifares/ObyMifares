from math import sqrt
a = int(input())
b = int(input())
c = int(input())
p = (a  + b + c) / 2
print(sqrt( p*(p-a)*(p-b)*(p-c) ))
