a = float(input())
b = float(input())
q = input()
if q == '-':
    print(a - b)
elif q == '+':
    print(a + b)
elif q == '*':
    print(a * b)
elif q == '/':
    if b != 0:
        print(a / b)
    elif b == 0:
        print('888888')
else:
    print('888888')
