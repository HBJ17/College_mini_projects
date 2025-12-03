flights = {}   
passengers = {} 
bookings = {}   

next_booking_id = 1



def display_flight(flight_id, flight):
    print(f"  Flight ID     : {flight_id}")
    print(f"  Airline     : {flight['airline']}")
    print(f"  Origin      : {flight['origin']}")
    print(f"  Destination : {flight['destination']}")
    print(f"  Seats Left  : {flight['available_seats']}")
    print("-" * 40)


def display_passenger(passenger_id, passenger):
    print(f" Passenger ID  : {passenger_id}")
    print(f"  Name        : {passenger['name']}")
    print(f"  Contact     : {passenger['contact']}")
    print("-" * 40)


def display_booking(booking_id, booking):
    print(f" Booking ID    : {booking_id}")
    print(f"  Passenger ID: {booking['passenger_id']}")
    print(f"  Flight ID   : {booking['flight_id']}")
    print(f"  Status      : {booking['status']}")
    print("-" * 40)



def add_flight():
    flight_id = input("Enter new Flight ID: ").strip()
    if flight_id in flights:
        print("Flight with this ID already exists!")
        return

    airline = input("Enter Airline Name: ")
    origin = input("Enter Origin City: ")
    destination = input("Enter Destination City: ")

    try:
        available_seats = int(input("Enter Number of Available Seats: "))
        if available_seats < 0:
            raise ValueError
    except ValueError:
        print("Invalid seat number! Flight not added.")
        return

    flights[flight_id] = {
        "flight_id": flight_id,
        "airline": airline,
        "origin": origin,
        "destination": destination,
        "available_seats": available_seats,
    }
    print("Flight added successfully!")


def update_seats_after_booking(flight_id):
    if flights[flight_id]["available_seats"] > 0:
        flights[flight_id]["available_seats"] -= 1
        return True
    else:
        return False


def update_seats_after_cancellation(flight_id):
    flights[flight_id]["available_seats"] += 1


def change_flight_route():
    flight_id = input("Enter Flight ID to modify: ").strip()
    if flight_id not in flights:
        print("No such flight.")
        return

    print("Current route:")
    print(f"Origin      : {flights[flight_id]['origin']}")
    print(f"Destination : {flights[flight_id]['destination']}")

    new_origin = input("Enter new Origin (press Enter to keep same): ").strip()
    new_destination = input("Enter new Destination (press Enter to keep same): ").strip()

    if new_origin:
        flights[flight_id]["origin"] = new_origin
    if new_destination:
        flights[flight_id]["destination"] = new_destination

    print("Route updated successfully.")


def display_all_flights():
    if not flights:
        print("No flights in database.")
        return
    print()
    print("    All Flights   ")
    for fid, frec in flights.items():
        display_flight(fid, frec)


def add_passenger():
    passenger_id = input("Enter new Passenger ID: ").strip()
    if passenger_id in passengers:
        print("Passenger with this ID already exists!")
        return

    name = input("Enter Passenger Name: ")
    contact = input("Enter Contact Details (phone/email): ")

    passengers[passenger_id] = {
        "passenger_id": passenger_id,
        "name": name,
        "contact": contact,
    }

    print("Passenger added successfully!")


def display_all_passengers():
    if not passengers:
        print("No passengers in database.")
        return
    print()
    print("    All Passengers    ")
    for pid, prec in passengers.items():
        display_passenger(pid, prec)



def book_flight():
    global next_booking_id

    passenger_id = input("Enter Passenger ID: ").strip()
    if passenger_id not in passengers:
        print("Passenger does not exist! Please add passenger first.")
        return

    flight_id = input("Enter Flight ID to book: ").strip()
    if flight_id not in flights:
        print("Flight does not exist!")
        return

    if not update_seats_after_booking(flight_id):
        print("No seats available on this flight!")
        return

    booking_id = f"B{next_booking_id}"
    next_booking_id += 1

    bookings[booking_id] = {
        "booking_id": booking_id,
        "passenger_id": passenger_id,
        "flight_id": flight_id,
        "status": "CONFIRMED",
    }

    print(f"Booking successful! Your Booking ID is {booking_id}")


def cancel_booking():
    booking_id = input("Enter Booking ID to cancel: ").strip()
    if booking_id not in bookings:
        print("No such booking.")
        return

    booking = bookings[booking_id]

    if booking["status"] == "CANCELLED":
        print("Booking is already cancelled.")
        return

    flight_id = booking["flight_id"]
    update_seats_after_cancellation(flight_id)
    booking["status"] = "CANCELLED"

    print("Booking cancelled and seat restored.")


def display_all_bookings():
    if not bookings:
        print("No bookings in system.")
        return
    print("\n--- All Bookings ---")
    for bid, brec in bookings.items():
        display_booking(bid, brec)



def main_menu():
    while True:
        print()
        print(" FLIGHT RESERVATION SYSTEM")
        print("1. Add New Flight")
        print("2. Change Flight Route")
        print("3. Show All Flights")
        print("4. Add New Passenger")
        print("5. Show All Passengers")
        print("6. Book a Flight")
        print("7. Cancel a Booking")
        print("8. Show All Bookings")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_flight()
        elif choice == "2":
            change_flight_route()
        elif choice == "3":
            display_all_flights()
        elif choice == "4":
            add_passenger()
        elif choice == "5":
            display_all_passengers()
        elif choice == "6":
            book_flight()
        elif choice == "7":
            cancel_booking()
        elif choice == "8":
            display_all_bookings()
        elif choice == "9":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


main_menu()
