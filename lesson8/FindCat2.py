line = 0
word = input()
for i in range(10):
	word = input()
	if word == 'СТОП':
		break
	line += 1
if 'КОТ' or 'кот' in word:
	print('МЯУ')
	print(line)
else:
	print('-1')
