#1.
def add(a:int,b:int)-> int:
   return a + b
a = int(input("a:"))
b = int(input("b:"))
print("a+b={}",format(add(a+b)))
#2.
N = int(input(""))
if N >=0 and N % 10 != 0:
   a = str(N)[::-1]
   print(a)
elif N < 0 and N % 10 != 0:
   b = -N
   c = str(b)[::-1]
   i = -int(c)
   print(i)
elif N >= 0 and N % 10 == 0:
   d = N // 10
   f = str(d)[::-1]
   print(f)
elif N < 0 and N % 10 == 0:
   g = N // 10
   h = str(-g)[::-1]
   j = -int(h)
   print(j)
#3.
str = (input(""))
num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0
for i in str:
    if i == '0':
        num_0 += 1
    elif i == '1':
        num_1 += 1
    elif i == '2':
        num_2 += 1
    elif i == '3':
        num_3 += 1
    elif i == '4':
        num_4 += 1
    elif i == '5':
        num_5 += 1
    elif i == '6':
        num_6 += 1
    elif i == '7':
        num_7 += 1
    elif i == '8':
        num_8 += 1
    elif i == '9':
        num_9 += 1
print(f'num_0: {num_0}\nnum_1: {num_1}\nnum_2: {num_2}\nnum_3: {num_3}\nnum_4: {num_4}\nnum_5: {num_5}\nnum_6: {num_6}\nnum_7: {num_7}\nnum_8: {num_8}\nnum_9: {num_9}')
#4.
# 变量初始化
total_scholarships = 0
max_scholarship = 0
student_with_max_scholarship = None
students = []
# 定义计算奖学金的函数
def calculate_scholarship(student):
    scholarships = {
        'academician': 8000,
        'youth': 4000,
        'excellent': 2000,
        'west': 1000,
        'class_contribution': 850
    }
    total = 0
    if student['average'] > 80 and student['publications'] >= 1:
        total += scholarships['academician']
    if student['average'] > 85 and student['class_assessment'] > 80:
        total += scholarships['youth']
    if student['average'] > 90:
        total += scholarships['excellent']
    if student['average'] > 85 and student['west_province']:
        total += scholarships['west']
    if student['class_assessment'] > 80 and student['class_leader']:
        total += scholarships['class_contribution']
    return total
N = int(input("学生总数：\n"))
for _ in range(N):
    student_input = input().split()
    name = student_input[0]
    average = int(student_input[1])
    class_assessment = int(student_input[2])
    class_leader = student_input[3] == 'Y'
    west_province = student_input[4] == 'Y'
    publications = int(student_input[5])

    student_data = {
        'name': name,
        'average': average,
        'class_assessment': class_assessment,
        'class_leader': class_leader,
        'west_province': west_province,
        'publications': publications
    }
    students.append(student_data)
    scholarship = calculate_scholarship(student_data)
    total_scholarships += scholarship
    if scholarship > max_scholarship:
        max_scholarship = scholarship
        student_with_max_scholarship = name
print(student_with_max_scholarship)
print(max_scholarship)
print(total_scholarships)
