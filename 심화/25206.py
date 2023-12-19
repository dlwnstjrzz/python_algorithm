# 학점의 총합
grades = 0
# average
average = 0
grade_dic = {
    'A+':	4.5,
    'A0':	4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F': 0}

while True:
    user_input = input()
    if user_input != '':
        course, total, grade = map(str, user_input.split())
    else:
        break
    if grade != 'P':
        grades += float(total)
        average += float(total) * grade_dic[grade]
print(average / grades)
