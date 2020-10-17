price = float(input())
total = 0
while price > 0:
    if price > 1000:
        price *= 0.95
    total += price
    price = float(input())
print(total)
