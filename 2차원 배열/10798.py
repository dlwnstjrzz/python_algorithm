maxLen = 0
matrix = [[] for a in range(5)]
for i in range(5):
    word = input()
    maxLen = max(maxLen, len(word))
    matrix[i] = word
n_list = []
for i in range(maxLen):
    for j in range(5):
        if len(matrix[j])-1 >= i:
            n_list.append(matrix[j][i])
print(''.join(n_list))

# input()을 한번에 넣는 방법
matrix = [input() for a in range(5)]
