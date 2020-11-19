word = input()
shortest = longest = word
while word != 'стоп':
    if len(word) < len(shortest):
        shortest = word
    elif len(word) > len(longest):
        longest = word
    word = input()
if set(shortest) <= set(longest):
    print('ДА')
else:
    print('НЕТ')