n, m = map(int, input().split())
balls = ['0' for i in range(n)]

for l in range(m):
    i, j, k = map(int, input().split())
    for t in range(i-1, j):
        balls[t] = str(k)

print(' '.join(balls))
