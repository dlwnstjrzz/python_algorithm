word = input()
alpha = [0 for _ in range(26)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in word:
    index = alphabet.find(i)
    alpha[index] += 1
    numbers = map(str, alpha)
print(' '.join(numbers))
#  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
