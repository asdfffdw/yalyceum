num = 1000
print('500')
while True:
    use = input()
    if use == '<':
        num = num - (num / 2)
        print(round(num))
    elif use == '>':
        num = num + (num / 2)
        print(round(num))
    elif use == '=':
        print(round(num))
        exit()
    else:
        print('Неверный ввод, попробуйте еще раз')
