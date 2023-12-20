N = int(input())

for i in range(N):
    stack = []
    word = input()
    for j in word:
        if j == '(':
            stack.append(word)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                stack.append('false')
                break

    if not stack:
        print('YES')
    else:
        print('NO')
