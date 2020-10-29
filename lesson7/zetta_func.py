n = int(input())
k = float(0)
for n in range(1, n + 1):
    k = k + (1 / n ** 2)
num = 3.141592653589793 ** 2 / float(k)
print(float(num))