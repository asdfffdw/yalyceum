login = input()
mail = input()
if '@' not in mail:
    print('Некорректный адреc')
elif '@' in login:
    print('Некорректный логин')
else:
    print('OK')