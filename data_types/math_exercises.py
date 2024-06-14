from math import pow, sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


result = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
print(result)
