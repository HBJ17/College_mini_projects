def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with open("contacts.txt", "a") as f:
        f.write(name + " - " + phone + "\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            print(f.read())
    except:
        print("File not found")

def search_contact():
    name = input("Enter name to search: ")
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                if line.startswith(name):
                    print(line)
    except:
        print("File error")

def delete_contact():
    name = input("Enter name to delete: ")
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
        with open("contacts.txt", "w") as f:
            for line in lines:
                if not line.startswith(name):
                    f.write(line)
    except:
        print("File error")

while True:
    print("\nPhone Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
        