x = False
kolvo = int(input())
for i in range(kolvo):
    fraza = input()
    if 'Пёс' in fraza or 'пёс' in fraza:
        x = False
    elif 'Кот' in fraza or 'кот' in fraza:
        x = True
if x:
    print('МЯУ')
else:
    print('НЕТ')