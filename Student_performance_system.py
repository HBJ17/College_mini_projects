# Student Performance Management System

#a
def add_student(roll, name, marks):
    total = sum(marks)
    average = total / len(marks)
    return (name, marks, total, average)


#c
def grade_student(average):
    if average >= 90:
        return "Grade A"
    elif average >= 75:
        return "Grade B"
    elif average >= 60:
        return "Grade C"
    else:
        return "Fail"

#b

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i + 1}")
    roll = int(input("Roll Number: "))
    name = input("Name: ")
    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))

    marks = (m1, m2, m3)
    students[roll] = add_student(roll, name, marks)

#d

passed_students = []

for roll, data in students.items():
    if data[3] >= 60:
        passed_students.append(data[0])

#f

file = open("students.txt", "w")
file.write("Roll | Name | Marks | Total | Average | Grade\n")

for roll, data in students.items():
    name, marks, total, avg = data
    grade = grade_student(avg)
    file.write(f"{roll} | {name} | {marks} | {total} | {avg:.2f} | {grade}\n")

file.close()

print("\n    Student File Content    ")
file = open("students.txt", "r")
print(file.read())
file.close()

#g

highest_total = max(students[roll][2] for roll in students)

print("Students with Highest Total Marks:")
for roll, data in students.items():
    if data[2] == highest_total:
        print(f"Roll: {roll}, Name: {data[0]}, Total: {data[2]}")

#e
while True:
    print("\n    Options    ")
    print("1. Display all student details")
    print("2. Display passed students")
    print("3. Search student by roll number")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for roll, data in students.items():
            name, marks, total, avg = data
            grade = grade_student(avg)
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}, "
                  f"Total: {total}, Average: {avg:.2f}, Grade: {grade}")

    elif choice == 2:
        print("Passed Students:")
        for name in passed_students:
            print(name)

    elif choice == 3:
        search_roll = int(input("Enter roll number: "))
        if search_roll in students:
            data = students[search_roll]
            grade = grade_student(data[3])
            print(f"Roll: {search_roll}, Name: {data[0]}, Marks: {data[1]}, "
                  f"Total: {data[2]}, Average: {data[3]:.2f}, Grade: {grade}")
        else:
            print("Invalid roll number!")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
