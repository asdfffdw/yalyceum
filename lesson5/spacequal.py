s = input()
max_h = 149
min_h = 191
k = 0
while s != '!':
    height = int(s)
    if 150 <= height <= 190:
        k += 1
        if height > max_h:
            max_h = height
        if height < min_h:
            min_h = height
    s = input()
print(k)
print(min_h, max_h)
