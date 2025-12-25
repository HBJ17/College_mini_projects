submissions = []

def add_submission(name, subject, marks, day):
    status = "Pass" if marks >= 50 else "Fail"
    return {
        "name": name,
        "subject": subject,
        "marks": marks,
        "day": day,
        "status": status
    }

n = int(input("Enter number of submissions: "))
for _ in range(n):
    name = input("Student Name: ")
    subject = input("Subject: ")
    marks = int(input("Marks Obtained: "))
    day = int(input("Submission Day: "))
    submissions.append(add_submission(name, subject, marks, day))

failed_students = [s["name"] for s in submissions if s["status"] == "Fail"]

with open("assignments.txt", "w") as f:
    for s in submissions:
        f.write(f'{s["name"]},{s["subject"]},{s["marks"]},{s["day"]},{s["status"]}\n')

with open("assignments.txt", "r") as f:
    records = f.readlines()

while True:
    print("\n1. Display submissions")
    print("2. Search submission")
    print("3. Display failed students")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        for s in submissions:
            print(s)
    elif choice == "2":
        search_name = input("Enter student name to search: ")
        found = False
        for s in submissions:
            if s["name"].lower() == search_name.lower():
                print(s)
                found = True
        if not found:
            print("Submission not found")
    elif choice == "3":
        print(failed_students)
    elif choice == "4":
        break
    else:
        print("Invalid choice")

top_submission = submissions[0]
for s in submissions:
    if s["marks"] > top_submission["marks"]:
        top_submission = s

print("Highest Marks Submission:")
print(top_submission)
