num = int(input())
total = 0
while True:
    if num == 1:
        print(total)
        break

    if num % 3 == 0:
        num /= 3
    elif num % 2 == 0:
        if (num - 1) % 3 == 0 and num/2 % 2 != 0:
            num -= 1
        else:
            num /= 2
    else:
        num -= 1
    total += 1
