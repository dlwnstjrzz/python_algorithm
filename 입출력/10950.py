T = input()
numbers = []
while len(numbers) < int(T):
  a, b = map(int,input().split())
  numbers.append(a + b)

for sum in numbers:
  print(sum)