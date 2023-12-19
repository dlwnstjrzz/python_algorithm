num = int(input())

for i in range(1, num + 1):

    if i != num:
        print(' ' * (num - i - 1) + ' *' * i)
    else:
        print(('* ' * i).rstrip())
