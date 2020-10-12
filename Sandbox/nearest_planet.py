planet1 = input()
planet2 = input()
if (planet1 == 'Марс' and planet2 == 'Венера') or (planet1 == 'Венера' and planet2 == 'Марс'):
    print('Точно!')
elif (planet1 == 'Венера' or planet2 == 'Марс') or (planet1 == 'Марс' or planet2 == 'Венера'):
    print('Почти правильно.')
else:
    print('Ну нет, это не так!')
