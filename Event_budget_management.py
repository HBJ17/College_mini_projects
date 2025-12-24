events = []
over_budget_events = []

def add_event(event_id, name, budget, spent):
    balance = budget - spent
    status = "Within Budget"
    if spent > budget:
        status = "Over Budget"
        over_budget_events.append(name)

    event = {
        "Event ID": event_id,
        "Name": name,
        "Budget": budget,
        "Spent": spent,
        "Balance": balance,
        "Status": status
    }
    events.append(event)

n = int(input("Enter number of events: "))

for i in range(n):
    event_id = input("Event ID: ")
    name = input("Event Name: ")
    budget = float(input("Budget Allocated: "))
    spent = float(input("Amount Spent: "))
    add_event(event_id, name, budget, spent)

def write_to_file():
    with open("events.txt", "w") as file:
        for e in events:
            file.write(
                f"{e['Event ID']},{e['Name']},{e['Budget']},"
                f"{e['Spent']},{e['Balance']},{e['Status']}\n"
            )

def read_from_file():
    with open("events.txt", "r") as file:
        for line in file:
            print(line.strip())

def highest_expenditure():
    max_event = events[0]
    for e in events:
        if e["Spent"] > max_event["Spent"]:
            max_event = e
    print(max_event)

while True:
    print("\n1. Display all events")
    print("2. Search event")
    print("3. Display over-budget events")
    print("4. Write and read file")
    print("5. Highest expenditure event")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for e in events:
            print(e)

    elif choice == "2":
        name = input("Enter event name: ")
        found = False
        for e in events:
            if e["Name"].lower() == name.lower():
                print(e)
                found = True
        if not found:
            print("Event not found")

    elif choice == "3":
        if over_budget_events:
            for name in over_budget_events:
                print(name)
        else:
            print("No over-budget events")

    elif choice == "4":
        write_to_file()
        read_from_file()

    elif choice == "5":
        highest_expenditure()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
