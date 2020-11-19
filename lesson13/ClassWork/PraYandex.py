n = int(input())
lines = []
for i in range(n):
    lines.append(input())
search_line = input()
for i in lines:
    if search_line in i:
        print(i)