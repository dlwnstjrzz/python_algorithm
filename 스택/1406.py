# L이면 pop해서 새 스택에 push해놓음
# D이면 새 스택에 push해 놓은걸 pop해서 원래 스택에 push함
# B이면 원래 스택에서 pop함
# P면 문자를 스택에 push함
# 모든 과정이 끝나고 원래 스택에 새 스택에서 하나씩 pop해서 push해줌
# 스택은 삽입 삭제가 O(1)이므로 커서 기준 왼쪽 오른쪽으로 스택을 2개 사용해서 문제를 푼다
word = input()
n = int(input())
stack = [i for i in word]
temp = []
for i in range(n):
    user_input = input()
    if user_input == 'L':
        if stack:
            num = stack.pop()
            temp.append(num)
    elif user_input == 'D':
        if temp:
            num = temp.pop()
            stack.append(num)
    elif user_input == 'B':
        if stack:
            stack.pop()
    elif user_input[0] == 'P':
        letter = user_input[2]
        stack.append(letter)

while len(temp):
    stack.append(temp.pop())

print(''.join(stack))
