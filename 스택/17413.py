# 글자를 하나씩 스택에 넣는다
# 띄어쓰기가 나오면 지금까지 들어온 글자를 반대로 pop해서 출력한다
# <가 나왔을 때 스택에 글자가 들어있으면 pop해서 반대로 출력하고 다음 단계를 진행한다
# <가 나오면 >가 나올때까지 스택에 집어넣고 >가 나오면 그대로 출력한다

word = input()

stack = []

for i in word:
    if i == ' ' and '<' not in stack:
        temp = ''
        for i in range(len(stack)):
            temp += stack.pop()
        print(temp, end=' ')
    elif i == '<':
        if stack:
            temp = ''
            for j in range(len(stack)):
                temp += stack.pop()
            print(temp, end='')
        stack.append(i)
    elif i == '>':
        stack.append(i)
        print(''.join(stack), end='')
        for i in range(len(stack)):
            stack.pop()
    else:
        stack.append(i)
if stack:
    print(''.join(reversed(stack)), end='')
