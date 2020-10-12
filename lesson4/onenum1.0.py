number = float(input())
if -0.000001 < number < 0.000001:
	print(1000000.0)
else:
	print(1 / number)