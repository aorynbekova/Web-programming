def scores(students):
    array = list(input().split())
    average = sum(map(float, array[1]+array[3]+array[3])) / 3
    name = array[0]
    students[name] = average


n = int(input())
students = {}
for i in range(n):
    scores(students)
print('%.2f' % students[input()])