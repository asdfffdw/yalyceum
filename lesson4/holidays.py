city1 = input()
city2 = input()
city1_ok = 'Тула'
city2_ok = 'Пенза'
if city1 != city2 and (city1 == city1_ok and city2 != city2_ok
                       or city2 == city2_ok and city1 != city2_ok):
    print('ДА')
else:
    print('НЕТ')
