import sys
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c
x1 = (-b - sqrt(d))/(2*a)
x2 = (-b + sqrt(d))/(2*a)

print(int(x1))
print(int(x2))
