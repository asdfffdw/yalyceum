word = input()
while word != 'пока' or word != 'до свидания' or word != 'до встречи' or word != 'до связи':
    if 'привет' in word or 'здравст' in word:
        print('Приветствую вас в программе бот-говорилка! Продолжайте разговор')
    elif 'как дела' in word:
        print('Нормально, а у тебя?')
