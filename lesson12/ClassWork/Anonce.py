leng = int(input())
n = int(input())
for i in range(n):
    heading = input()
    if len(heading) > leng:
        print(heading[:leng - 3] + '...')
    else:
        print(heading)