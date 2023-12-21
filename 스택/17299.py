N = int(input())

arr = list(map(int, input().split()))

n_dic = {}

for i in arr:
    n_dic[i] = n_dic.get(i, 0) + 1
answer = [-1 for _ in range(N)]
stack = []
for i in range(N):
    while stack and n_dic[arr[stack[-1]]] < n_dic[arr[i]]:
        answer[stack.pop()] = arr[i]

    stack.append(i)

print(*answer)
