import math
N = int(input())
num = list(map(int, input().split()))

numPrime = 0
for i in num:
    isPrime = True
    if i != 1:
        for j in range(2, math.ceil(i/2) + 1):

            if i % j == 0:
                isPrime = False
        if isPrime:
            numPrime += 1

print(numPrime)
