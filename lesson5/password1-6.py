password1 = input()
password2 = input()
lpasswrd = len(password1)
if lpasswrd < 8:
    print('Короткий!')
    quit()
elif '123' in password1:
    print('Простой')
elif password1 != password2:
    print('Различаются.')
else:
    print('OK')
