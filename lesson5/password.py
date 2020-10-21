password1 = input()
password2 = input()
x = False
while x is False:
    if len(password1) < 8:
        print('Короткий!')
    elif '123' in password1:
        print('Простой!')
    elif password1 != password2:
        print('Различаются.')
    else:
        print('OK')
        x = True
        quit()
    password1 = input()
    password2 = input()

