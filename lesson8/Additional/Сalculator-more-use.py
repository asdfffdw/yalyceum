stop = 0
use = ''
result = 0
while True:
    num1 = int(input())
    use = input()
    if use == '-':
        num2 = int(input())
        result = num1 - num2
        print(result)
    if use == 'x':
        print(num1)
        break
    if use == '+':
        num2 = int(input())
        result = num1 + num2
        print(result)
    if use == '*':
        num2 = int(input())
        result = num1 * num2
        print(result)
    if use == '/':
        num2 = int(input())
        if num2 == 0:
            continue
        result = num1 // num2
        print(result)
    if use == '%':
        num2 = int(input())
        if num2 == 0:
            continue
        result = num1 % num2
        print(result)
    if use == '!':
        if num1 == -1:
            continue
        if num1 == 0:
            num1 = 1
        for i in range(1, num1):
            num1 *= i
        print(num1)



