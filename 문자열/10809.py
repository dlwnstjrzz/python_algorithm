# word = input()

# numList = [-1 for _ in range(26)]
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in word:
#     index = word.find(i)
#     index2 = alphabet.find(i)
#     numList[index2] = index

# print(' '.join(map(str, numList)))

for index, char in enumerate(word):
    if numList[ord(char) - ord('a')] == -1:
        numList

S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end=' ')
