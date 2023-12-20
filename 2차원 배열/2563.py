N = int(input())
# False로 된 100 * 100 2차원 배열 생성
# x부터 x+10까지 돌면서 True로 채움
# True의 개수를 세면 됨
n_list = [[False for a in range(100)] for a in range(100)]

for i in range(N):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x+10):
            n_list[j][i] = True
total = 0
for i in n_list:
    total += i.count(True)

print(total)
