a = 1

while a:
  a, b = map(int, input().split())
  if a != 0:
    print(a + b)