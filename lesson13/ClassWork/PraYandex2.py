lines = [input() for i in range(int(input()))]
search_lines = [input() for i in range(int(input()))]
for line in lines:
    for search_line in search_lines:
        if search_line not in line:
            break
    else:
        print(line)