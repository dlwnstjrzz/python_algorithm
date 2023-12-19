rest = []
for i in range(10):
    rest.append(int(input()) % 42)

rest.sort()
prev = -1
total = 0
for i in rest:
    if i != prev:
        total += 1
    prev = i
print(total)


rest = []
for i in range(10):
    a = int(input())
    if a % 42 not in rest:
        rest.append(a % 42)

print(len(rest))
