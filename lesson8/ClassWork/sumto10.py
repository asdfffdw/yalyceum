sum_ = 0
a = int(input())
count_ = 1
while a != 0:
    sum_ += a
    if sum_ == 10:
        print(count_) 
        break
    count_ += 1
    a = int(input())