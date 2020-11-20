import math
a = float(input())
v = float(input())
count = 0
if a < v:
    print(count)
    exit()
while not abs(a - v) <= 0.01:
    a = math.sqrt(v ** 2 + (a - v) ** 2)
    count += 1
print(count)