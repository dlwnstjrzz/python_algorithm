num = int(input())

for i in range(1, num+1):
    print('*' * i + ' ' * (2*num - 2*i) + '*' * i)

for i in range(num+1, 2*num + 1):
    print('*' * (2*num-i) + ' ' * (2*num - 2 * (2*num-i)) + '*' * (2*num-i))
