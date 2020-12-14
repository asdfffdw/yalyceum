num = [int(input()) for _ in range(int(input()))]
min, max = int(input()), int(input())
for elem in num:
    if min <= elem <= max:
        print(elem)