maxNum = 0

targetIndex = 0
for i in range(1, 10):
    n = int(input())
    if n > maxNum:
        maxNum = n
        targetIndex = i

print(f'{maxNum}\n{targetIndex}')


l = [int(input()) for a in range(9)]
print(l)
