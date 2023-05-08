list = []

n = int(input("Enter the number of tuples:"))

max_grade = 0
max_student_name = ""

for i in range(n):
    name = input("Enter student name:")
    grade = float(input("Enter grade:"))

    list.append((name, grade))

    if(grade > max_grade):
        max_grade = grade
        max_student_name = name

print("The max student name is: " + max_student_name)
print("The max student grade is: " + str(max_grade))
