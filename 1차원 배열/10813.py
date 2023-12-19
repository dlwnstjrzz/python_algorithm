n, m = map(int, input().split())

balls = [str(i) for i in range(1, n+1)]

for t in range(m):
    i, j = map(int, input().split())
    balls[i - 1], balls[j - 1] = balls[j - 1], balls[i - 1]

print(' '.join(balls))
