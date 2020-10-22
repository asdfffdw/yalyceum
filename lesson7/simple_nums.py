num = int(input())
count = 0

for i in range(1, num + 1):
    if (num % i) == 0:
        print(i, end=' ')
        count += 1
if count > 2 or count == 1:
    print('\nНЕТ')
else:
    print('\nПРОСТОЕ')

