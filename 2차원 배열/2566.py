maxNum = 0
maxCoor = [0, 0]
for i in range(9):
    row = list(map(int, input().split()))
    rowMax = max(row)
    if rowMax >= maxNum:
        maxNum = rowMax
        maxCoor = [i+1, row.index(maxNum)+1]

print(maxNum)
print(' '.join(map(str, maxCoor)))
