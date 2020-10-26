x = int(input())
i = 1
while i <= x:
    i += 1
    y = input()
    if 'Кот' in y or 'кот' in y:
        print('МЯУ')
        exit()
if 'кот' not in y or "Кот" not in y:
    print("НЕТ")
