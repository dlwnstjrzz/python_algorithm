n, m = map(int, input().split())

buckets = [i+1 for i in range(n)]

for l in range(m):
    i, j = map(int, input().split())
    temp = buckets[i-1:j]
    temp.reverse()
    buckets[i-1:j] = temp

print(' '.join(map(str, buckets)))
