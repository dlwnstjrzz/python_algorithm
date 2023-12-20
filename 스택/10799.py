# (가 나오면 우선 스택에 넣고 파이프 개수 + 1
# )가 나왔는데 스택에서 pop한게 (이면 파이프 개수 -1하고 전체 점수 += 파이프 개수
# )가 나왔는데 스택에서 pop한게 )이면 파이프 개수 -1하고 전체 점수 + 1

stack = []
pipe = 0
total = 0
test = []
for i in input():
    test.append(i)
    if i == '(':
        stack.append(i)
        pipe += 1
    elif i == ')':
        last = stack.pop()
        if last == '(':
            pipe -= 1
            total += pipe
        else:
            pipe -= 1
            total += 1
        stack.append(i)

print(total)
