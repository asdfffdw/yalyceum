num = int(input())
a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
d = num // 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a == 0 and b:
    a, b = b, a
else:
    a, c = c, a
print(d + 10 * (c + 10 * (b + 10 * a)))
