a = int(input())
b = 0
if a == 1:
    print(0)
while a > 1:
    a = a / 2
    b += 1
    if a == 1:
        print(b)
    elif a < 1:
        print('НЕТ')

