n, m = map(int, input().split())

matrix1 = [[] for a in range(n)]
matrix2 = [[] for a in range(n)]
for i in range(n):
    row = input().split()
    matrix1[i] = row

for j in range(n):
    row = input().split()
    matrix2[j] = row

answer = [[0 for a in range(m)] for a in range(n)]

for i in range(n):
    for j in range(m):
        answer[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])

for i in answer:
    print(' '.join(map(str, i)))
