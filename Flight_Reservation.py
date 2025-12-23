flights = {
    "1" : {
        "Airline": "IndiGo",
        "From": "Chennai",
        "To": "Delhi",
        "Seats": 120
    },


    "2" : {
        "Airline": "Air India",
        "From": "Mumbai",
        "To": "Bangalore",
        "Seats": 85
    }
}

def add_flight():
    fid = input("Flight ID: ")
    flights[fid] = {
        "airline": input("Airline: "),
        "origin": input("From: "),
        "destination": input("To: "),
        "available_seats": int(input("Seats: "))
    }

    print("Flight Added Successfully")

def update_seats():
    fid = input("Flight ID: ")
    flights[fid]["available_seats"] = int(input("New Seats: "))
    print("Seats Updated Successfully")

def change_route():
    fid = input("Flight ID: ")
    flights[fid]["destination"] = input("New Destination: ")
    print("Route Updated Successfully")

def display_flights():
    for f in flights.values():
        print(f)

while True:
    print("\nFlight Reservation System")
    print("1. Add Flight")
    print("2. Update Seats")
    print("3. Change Route")
    print("4. Display Flights")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_flight()
    elif choice == "2":
        update_seats()
    elif choice == "3":
        change_route()
    elif choice == "4":
        display_flights()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

