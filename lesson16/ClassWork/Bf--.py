n = 30_000
cells = [0] * n
i = 0
for c in input():
    if c == '>':
        i = (i + 1) % n
    elif c == '<':
        i = (i - 1) % n
    elif c == '+':
        cells[i] += 1
    elif c == '-':
        cells[i] -= 1
    else:
        print(cells[i] % 256)