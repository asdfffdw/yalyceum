word = input('Привет, какое у тебя настроение? ')

if ('хорош' in word) or ('норм' in word) or ('отличн' in word):
    print('Супер, рад за тебя')
elif ('плох' in word) or ('ужасн' in word):
    print('У меня тоже не очень')
else:
    print('Не совсем понятно что ты говоришь')