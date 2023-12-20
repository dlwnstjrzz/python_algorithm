N = int(input())

for i in range(N):
    word = map(str, input().split())

    for j in word:
        reversed = list(j)
        reversed.reverse()
        print(''.join(reversed), end=' ')
