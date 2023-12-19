word = input().lower()

maxNum = 0
correctLetter = ''
isMany = False
for trans in range(ord('a'), ord('z')+1):
    letter = chr(trans)
    num = word.count(letter)

    if maxNum < num:
        maxNum = num
        correctLetter = letter
        isMany = False
    elif maxNum == num:
        isMany = True

print(correctLetter.upper() if not isMany else '?')
