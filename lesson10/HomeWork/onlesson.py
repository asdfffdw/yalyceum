a = input()
x = []
for i in range(0, int(a)):
    x.append([])
    b = input()
    for j in range(0, int(b)):
        c = input()
        x[i].append(c)
y = x[0]
for k in x:
    y = list(set(y) & set(k))
print('\n\n')
for k in y:
    print(k)
