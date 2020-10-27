x = int(input())
i = 1
while i <= x:
	i += 1
	y = input()
	if ('Кот' in y) or ('кот' in y):
		print('МЯУ')
		break
if not ('кот' in y) or ('Кот' in y):
	print("НЕТ")
