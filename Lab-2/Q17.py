'''Admission to a professional course is subject to the following conditions:
(a) marks in Mathematics >= 60 (b) marks in Physics >=50
(c) marks in Chemistry >=40 (d) Total in all 3 subjects >=200
 (Or)
 Total in Maths & Physics>=150
Given the marks in the 3 subjects of n (user input) students, write a program to process 
the applications to list the eligible candidates.'''

n = int(input("Enter the number of students: "))
students = []
for i in range(n):
    student = []
    student.append(int(input("Enter the marks in Mathematics: ")))
    student.append(int(input("Enter the marks in Physics: ")))
    student.append(int(input("Enter the marks in Chemistry: ")))
    students.append(student)
eligible_students = []
for student in students:
    if student[0] >= 60 and student[1] >= 50 and student[2] >= 40 and sum(student) >= 200:
        eligible_students.append(student)
    elif student[0] >= 60 and student[1] >= 50 and sum(student[:2]) >= 150:
        eligible_students.append(student)
print("The eligible students are: ")
for student in eligible_students:
    print(student)


