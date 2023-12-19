month, day = map(int, input().split())

total = 0
for i in range(1, month + 1):
  if i != month:
    if i == 2:
      total += 28
    elif (i % 2 == 1 and i <= 7) or(i % 2 == 0 and i >= 8):
      total += 31
    else:
      total += 30
  else:
    total += day

if total % 7 == 1:
  print('MON')
if total % 7 == 2:
  print('TUE')
if total % 7 == 3:
  print('WED')
if total % 7 == 4:
  print('THU')
if total % 7 == 5:
  print('FRI')
if total % 7 == 6:
  print('SAT')
if total % 7 == 0:
  print('SUN')