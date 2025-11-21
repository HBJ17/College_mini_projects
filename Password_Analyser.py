#1
def classify_password(pwd):
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.islower() for ch in pwd)
    has_digit = any(ch.isdigit() for ch in pwd)
    has_special = any(not ch.isalnum() for ch in pwd)

    missing = []

    if not has_upper:
        missing.append("Add at least one uppercase letter")
    if not has_lower:
        missing.append("Add at least one lowercase letter")
    if not has_digit:
        missing.append("Add at least one digit")
    if not has_special:
        missing.append("Add at least one special character")

    if len(pwd) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong", missing
    elif len(pwd) >= 6 and (has_lower or has_upper) and has_digit:
        return "Moderate", missing
    else:
        return "Weak", missing


def Check_Paterns(password):
    find = password.find("123")
    count = password.count("1")
    start = password.startswith("A")
    end = password.endswith("Z")   

    if find != -1:               
        print("Your password contains 123")
    else:
        print("Your password does not contain 123")

    if count:
        print(f"Your password contains '1' {count} times.")

    if start:
        print("Your password starts with A")
    else:
        print("Your password does not start with A")

    if end:
        print("Your password ends with Z")
    else:
        print("Your password does not contain Z")


a = 0
while a < 3:
    password = input("Enter password: ")
    a += 1

    category, missing_info = classify_password(password)
    print("Password Strength:", category)
 

    if category == "Strong":
        print("Password accepted in", a, "attempt(s).")
        Check_Paterns(password)  
        break
    else:
        print("Feedback:")
        for msg in missing_info:
            print("=>", msg)
        print("Attempts left:", 3 - a)
else:
    print("Maximum attempts reached. Password not accepted.")

