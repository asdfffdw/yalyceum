n = int(input())
while True:
    a = n % 4 if n % 4 else 1
    if n < 3:
        a = n
    if a < 1:
        a = 1
    n -= a
    print(a, n)
    if n == 0:
        print('ИИ выиграл!')
        break
    b = int(input())
    while b > 3 or b < 1:
        print('Некорректный ход:', b)
        b = int(input())
    n -= b
    print(b, n)
    if n == 0:
        print('Вы выиграли!')
        break
