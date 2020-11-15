patient = int(input())
num = 0
while num != patient:
    stop = 0
    count = 0
    while stop != 1:
        word = input()
        if word == 'раз':
            count += 1
        elif word != 'раз':
            num += 1
            count = str(count)
            print('Правильных отсчётов было', count + ',', 'но теперь вы ошиблись.')
            break
        word = input()
        if word == 'два':
            count += 1
        elif word != 'два':
            num += 1
            count = str(count)
            print('Правильных отсчётов было', count + ',', 'но теперь вы ошиблись.')
            break
        word = input()
        if word == 'три':
            count += 1
        elif word != 'три':
            num += 1
            count = str(count)
            print('Правильных отсчётов было', count + ',', 'но теперь вы ошиблись.')
            break
        word = input()
        if word == 'четыре':
            count += 1
        elif word != 'четыре':
            num += 1
            count = str(count)
            print('Правильных отсчётов было', count + ',', 'но теперь вы ошиблись.')
            break
print('На сегодня хватит.')



