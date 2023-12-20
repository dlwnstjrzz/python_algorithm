# 우선 큐에 전부 숫자를 넣고
# K씩 pop한다
# k번째 pop은 버리고 나머지는 다시 push함
# push했을 때 큐에 있는 숫자 개수가 3미만이면 남은 숫자는 순서대로 넣는다
N, K = map(int, input().split())

answer = []
queue = [i for i in range(1, N+1)]
num = 0
for i in range(N):
    num += (K - 1)
    if num >= len(queue):
        num = num % len(queue)
    answer.append(queue.pop(num))

print(f"<{', '.join(map(str,answer))}>")
