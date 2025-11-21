confirmed_passengers = []
waiting_list = []

lim = 5

def book_ticket(name):
    if len(confirmed_passengers) < lim:
        confirmed_passengers.append(name)
        print(f"Ticket Confirmed for {name}")
    else:
        waiting_list.append(name)
        print(f"No seats, {name} added to Waiting List")

def view_lists():
    print()
    print("Confirmed Passengers:", confirmed_passengers)
    print("Waiting List:", waiting_list)
    print()

def cancel_ticket(name):
    if name in confirmed_passengers:
        confirmed_passengers.remove(name)
        print(f"Ticket Cancelled for {name}")

        if waiting_list:
            moved = waiting_list.pop(0)
            confirmed_passengers.append(moved)
            print(f"{moved} moved from waiting list to confirmed list.")
    elif name in waiting_list:
        waiting_list.remove(name)
        print(f"{name} removed from waiting list.")
    else:
        print("Passenger not found.")

while True:
    print("1. Book Ticket")
    print("2. View Lists")
    print("3. Cancel Ticket")
    print("4. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter passenger name: ")
        book_ticket(name)

    elif ch == 2:
        view_lists()

    elif ch == 3:
        name = input("Enter passenger name to cancel: ")
        cancel_ticket(name)

    elif ch == 4:
        break

    else:
        print("Invalid Choice")
