# nCr 구하고
# 뒤부터 0세면됨

n, r = map(int, input().split())


def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    else:
        return 1


combination = str(int(factorial(n)/(factorial(n-r)*factorial(r))))

count = 0
for i in range(len(combination)-1, 0, -1):

    if combination[i] == '0':
        count += 1
    else:
        print(count)
        break
