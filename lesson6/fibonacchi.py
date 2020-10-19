x = int(input())
old_fib = 1
u = 1
while old_fib <= x:
    print(old_fib)
    o = old_fib + u
    old_fib = u
    u = o