num = int(input())
student = []

for i in range(num):
    person = input().split()
    student.append([person[0], int(person[1])])

student = sorted(student, key=lambda x: x[1])

for i in range(num):
    print(student[i][0], end = ' ')