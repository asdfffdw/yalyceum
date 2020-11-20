for i in range(1, int(input()) + 1):
    rockets = i
    while i:
        print(f'Осталось секунд: {i - 1}')
        i -= 1
    print(f'Пуск {rockets}')