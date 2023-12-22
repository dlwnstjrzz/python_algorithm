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


# 제곱근을 이용한 판별
def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


# 에라토스테네스의 체
# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n+1) if array[i]]
# n이 100만 이내로 주어지는 경우 사용, 계산상 400만번 연산임
# 시간 복잡도 O(NloglogN)
