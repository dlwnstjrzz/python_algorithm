n, target = map(int, input().split())
n_list = list(map(int, input().split()))
answer = []
for i in n_list:
    if i < target:
        answer.append(str(i))

print(' '.join(answer))
