n = int(input())
for i in range(n):
    s = input()
    for j in range(len(s) - 2):
        if s[j:j + 3] == 'кот':
            print(i + 1, j + 1)
            break