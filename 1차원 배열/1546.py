n = int(input())
grades = list(map(int, input().split()))
maxGrade = max(grades)
total = 0
for i in grades:
    total += i/maxGrade*100

print(total/n)
