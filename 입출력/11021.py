t = int(input())

for i in range(1, t + 1):
  a, b = map(int, input().split())

  print(f'Case #{i}: {sum(map(int, input().split()))}')
  