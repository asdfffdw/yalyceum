a = set()
b = set()
num = input()
while num != '':
    a.add(num)
    num = input()
num = input()
while num != '':
    b.add(num)
    num = input()
intersection = a & b
if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)