word1, word2 = input(), input()
bulls = 0
for i in range(len(word1)):
    bulls += word1[i] == word2[i]
cows = len(set(word1) & set(word2)) - bulls
print(bulls, cows)