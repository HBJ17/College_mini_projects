# Contact Management System

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    with open("contacts.txt", "a") as f:
        f.write(f"{name} - {phone}\n")

    print("Contact added successfully!\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            data = f.read()
            if not data:
                print("Contact list is empty.\n")
            else:
                print("Contacts:\n", data)
    except FileNotFoundError:
        print("Contact file not found.\n")


def search_contact():
    name = input("Enter name to search: ").strip()
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                if line.startswith(name + " -"):
                    print("Found:", line)
                    return
            print("Contact not found.\n")
    except FileNotFoundError:
        print("File not found.\n")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()

        with open("contacts.txt", "w") as f:
            found = False
            for line in lines:
                if not line.startswith(name + " -"):
                    f.write(line)
                else:
                    found = True

        if found:
            print("Contact deleted successfully!\n")
        else:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


while True:
    print("1.Add Contact  2.View Contacts  3.Search Contact")
    print("4.Delete Contact  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice\n")
