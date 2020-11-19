n = int(input())
for i in range(n):
    advice = input()
    if advice[:3] == 'не ' or advice[:3] == 'Не ':
        advice = advice[3:]
    print(advice)