employees = []
n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    basic = float(input("Basic Pay: "))
    employees.append((emp_id, name, basic))

print()
print("Employees")
for emp in employees:
    print(emp)


gross_list = []
print()
print("Gross Salary")
for emp in employees:
    gross = emp[2] + 0.10 * emp[2] + 0.05 * emp[2]
    gross_list.append((emp, gross))
    print(f"{emp[1]} : Gross Salary = {gross}")


max_gross_emp= max(gross_list, key=lambda x: x[1])
print()
print(f"Employee with Maximum Gross Salary: {max_gross_emp[0][1]} : {max_gross_emp[1]}")


