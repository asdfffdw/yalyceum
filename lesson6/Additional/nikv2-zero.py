a = int(input())
while a > 0:
    b = a % 4
    if b == 0:
        b = 2
    print(b)
    a -= b
    print(a)
    if a == 0:
        print('Вы выиграли!')
    else:
        print()
        b = 0
        while not (1 <= b <= 3 and b <= a):
            b = int(input())
            if b > 3:
                print('Ошибка!')
        a -= b
        print(a)
        if a == 0:
            print('Вы проиграли!')