number_of_lines = int(input())
for i in range(0, number_of_lines):
    line = input()
    if 'Кот' or 'кот' in line:
        print('МЯУ')
        break
    else:
        print('НЕТ')