x = int(input())
for i in range(x):
    y = input()
    if 'Кот' in y or 'кот' in y:
        print('МЯУ')
        x = True
        break
    elif not 'Кот' and 'кот' in y:
        print('НЕТ')
        x = False
        continue
if x is True:
    exit()
else:
    print('НЕТ')
