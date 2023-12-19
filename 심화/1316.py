n = int(input())

total = 0
for i in range(n):
    alreadyHas = False
    n_list = [False for a in range(26)]
    word = input()

    prev = 0
    for j in word:
        index = ord(j) - 97
        if not n_list[index]:
            n_list[index] = True
        else:
            if prev != index:
                alreadyHas = True
                break
        prev = index
    if not alreadyHas:

        total += 1
print(total)

# 훨씬 간단한 방법
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)
