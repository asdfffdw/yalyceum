number = float(input())
if abs(number) < 1e-6:  # abs() - модуль числа
	print(1e-6)
else:
	print(1 / number)