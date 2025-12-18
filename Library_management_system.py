library = {}

def add_book():
    book_id = input("Book ID: ")
    library[book_id] = {
        "title": input("Title: "),
        "author": input("Author: "),
        "status": "Available",
        "section": input("Section: ")
    }

def update_status():
    book_id = input("Book ID: ")
    library[book_id]["status"] = input("New Status: ")

def transfer_section():
    book_id = input("Book ID: ")
    library[book_id]["section"] = input("New Section: ")

def display_books():
    for b in library.values():
        print(b)

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Status")
    print("3. Transfer Section")
    print("4. Display Books")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        update_status()
    elif choice == "3":
        transfer_section()
    elif choice == "4":
        display_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
