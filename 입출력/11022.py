t = int(input())
# Case #1: 1 + 1 = 2

for i in range(1, t + 1):
  a, b = map(int, input().split())
  print(f'Case #{i}: {a} + {b} =',a+b)