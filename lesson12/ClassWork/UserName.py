name = input()
for symb in name:
    if not('a' <= symb <= 'z' or '0' <= symb <= '9' or symb == '_'):
        print('Неверный символ:', symb)
        break
else:
    print('OK')