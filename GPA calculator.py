def calc_total(internal, external):
    total = (internal / 50) * 40 + (external / 100) * 60
    return total

def get_grade_point(total):
    if total >= 90:
        return "O", 10
    elif total >= 80:
        return "A+", 9
    elif total >= 70:
        return "A", 8
    elif total >= 60:
        return "B+", 7
    elif total >= 50:
        return "B", 6
    else:
        return "F", 0

def calculate_gpa():
    n = int(input("Enter number of subjects: "))
    total_grade_points = 0

    for i in range(1, n + 1):
        internal = float(input(f"Internal marks for subject {i} (out of 50): "))
        external = float(input(f"External marks for subject {i} (out of 100): "))

        total = calc_total(internal, external)
        grade, gp = get_grade_point(total)
        total_grade_points += gp

        print(f"Subject {i}: Total = {total:.2f}, Grade = {grade}, Grade Point = {gp}")

    gpa = total_grade_points / n
    print("\nOverall GPA =", round(gpa, 2))


calculate_gpa()
