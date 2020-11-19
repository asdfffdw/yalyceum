n = int(input())
numbers = list()
summ = 0
for i in range(n):
    num = int(input())
    numbers.append(num)
min_n = int(input())
max_n = int(input())
for num in numbers[min_n - 1:max_n]:
    summ += num
print(summ)