ln = 0
rn = 1001
x = 1
while x != 0:
    num = (ln + rn) // 2
    print(num)
    use = input()
    if use == "<":
        rn = num
    elif use == ">":
        ln = num
    elif use == '=':
        x -= 1
