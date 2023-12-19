countList = [False for a in range(30)]

for i in range(28):
    countList[int(input()) - 1] = True

firstIndex = countList.index(False)
print(firstIndex + 1)
print(countList.index(False, firstIndex + 1) + 1)
