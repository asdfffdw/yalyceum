client = []
proc = []
n = int(input())
for i in range(n):
    client.append(int(input()))
    print(client[i])
print()
for i in range(n):
    proc.append(client[i] * 3)
for i in proc:
    print(i)