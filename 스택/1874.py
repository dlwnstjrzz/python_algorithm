# 가장 앞에 있는 숫자까지 push하고
# 만들 수 있는 숫자는 바로 뺀다

N = int(input())
stack = []
cnt = 1
answer = []
temp = True
for i in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        temp = False
        break

if temp:
    for i in answer:
        print(i)
else:
    print('NO')
