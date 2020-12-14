newlist = [int(i) for i in input().split()]
sent = input().split()
print(' '.join(sent[i - 1] for i in newlist).capitalize())
