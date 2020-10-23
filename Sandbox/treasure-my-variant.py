x = int(input())
y = int(input())
word = input()
while (x != 0) and (y != 0):
	if word == 'вперёд':
		y = y - 1
		print(y)
	elif word == 'налево':
		x = x - 1
		print(x)
	elif word == 'разворот':
		y = -y
		print(y)
	elif word == 'направо':
		x = x + 1
		print(x)
	elif word == 'стоп':
		quit()
	else:
		print('Ошибка ввода, повторите попытку')
	word = input()