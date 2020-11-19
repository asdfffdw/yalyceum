num = int(input())
list1 = list()
for i in range(num):
    word = input()
    list1.append(word)
k = int(input())
for i in list1:
    if k <= len(i):
        print(i[k - 1], end='')

