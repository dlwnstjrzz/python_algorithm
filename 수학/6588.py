# 아리어쩌구 체로 n까지에서 소수들을 골라낸다ㅏ
# 그 소수들의 인덱스 + 1을 리스트에 저장한다
# 투포인터로 2개가 합이 되는지 찾는다

import sys
input = sys.stdin.readline


numbers = [True for _ in range(1000001)]
numbers[0] = False
numbers[1] = False
for i in range(2, int(1000000 ** 0.5)+1):
    if numbers[i]:
        for k in range(i+i, 1000001, i):
            numbers[k] = False


while True:
    num = int(input())
    if not num:
        break

    for i in range(2, num):
        if numbers[i] and numbers[num-i]:
            print(f'{num} = {i} + {num-i}')
            break
