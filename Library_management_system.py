library = {}  

def add_book():
    print()
    print("    Add New Book    ")
    book_id = input("Enter Book ID: ").strip()
    if book_id in library:
        print("A book with this ID already exists!")
        return

    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    section = input("Enter Section: ").strip()
    status = "Available"  

    book_record = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status,
        "section": section
    }

    library[book_id] = book_record
    print("Book added successfully!")


def update_book_status():
    print()
    print("    Update Book Status (Available/Issued)    ")
    book_id = input("Enter Book ID: ").strip()
    if book_id not in library:
        print("No book found with this ID.")
        return

    print(f"Current status: {library[book_id]['status']}")
    new_status = input("Enter new status (Available / Issued): ").strip()

    if new_status not in ["Available", "Issued"]:
        print("Invalid status! Please enter either 'Available' or 'Issued'.")
        return

    library[book_id]["status"] = new_status
    print("Book status updated successfully!")


def transfer_book_section():
    print()
    print("    Transfer Book to Another Section    ")
    book_id = input("Enter Book ID: ").strip()
    if book_id not in library:
        print("No book found with this ID.")
        return

    print(f"Current section: {library[book_id]['section']}")
    new_section = input("Enter new section: ").strip()

    library[book_id]["section"] = new_section
    print("Book section updated successfully!")


def display_all_books():
    print()
    print("    List of All Books    ")
    if not library:
        print("No books in the library yet.")
        return

    for book_id, book in library.items():
        print("-" * 40)
        print(f"Book ID   : {book['book_id']}")
        print(f"Title     : {book['title']}")
        print(f"Author    : {book['author']}")
        print(f"Status    : {book['status']}")
        print(f"Section   : {book['section']}")
    print("-" * 40)


def main():
    while True:
        print()
        print("       Library Management System       ")
        print("1. Add New Book")
        print("2. Update Book Availability Status")
        print("3. Transfer Book to Another Section")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book_status()
        elif choice == "3":
            transfer_book_section()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")



main()

