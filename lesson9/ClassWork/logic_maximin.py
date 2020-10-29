n = int(input())
max = 0
r = 1
for element in range(n):
    t = int(input())
    m = 1000000
    for element_2 in range(t):
        h = int(input())
        if m > h:
            m = h
    if max < m:
        max = m
        r = element + 1
print(r, max)