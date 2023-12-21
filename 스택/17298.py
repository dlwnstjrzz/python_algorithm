# 스택에 인덱스를 저장한다
# 스택의 인덱스에 해당하는 값이 다음값보다 크면 인덱스를 계속 넣는다
# 만약 작으면 계속 꺼내면서 해당 값보다 작을때까지 값을 넣는다

n = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)


print(*answer)
