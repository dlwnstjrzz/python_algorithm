h, m = map(int, input().split())
cookM = int(input())

h += (cookM + m) // 60
m = (cookM + m) % 60

h %= 24

print(f'{h} {m}')
