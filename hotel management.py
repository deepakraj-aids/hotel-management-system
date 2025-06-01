# Simple Hotel Management System

rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}

def show_menu():
    print("\n--- Hotel Management Menu ---")
    print("1. View Room Status")
    print("2. Book a Room")
    print("3. Checkout a Room")
    print("4. View Current Guests")
    print("5. Exit")

def view_rooms():
    print("\nRoom Status:")
    for room, guest in rooms.items():
        status = "Available" if guest is None else f"Occupied by {guest}"
        print(f"Room {room}: {status}")

def book_room():
    room = int(input("Enter room number to book: "))
    if room in rooms:
        if rooms[room] is None:
            name = input("Enter guest name: ")
            rooms[room] = name
            print(f"Room {room} successfully booked for {name}.")
        else:
            print("Room is already occupied.")
    else:
        print("Invalid room number.")

def checkout_room():
    room = int(input("Enter room number to checkout: "))
    if room in rooms:
        if rooms[room] is not None:
            print(f"Room {room} checked out from {rooms[room]}.")
            rooms[room] = None
        else:
            print("Room is already available.")
    else:
        print("Invalid room number.")

def view_guests():
    print("\nCurrent Guests:")
    for room, guest in rooms.items():
        if guest is not None:
            print(f"Room {room}: {guest}")
    if all(guest is None for guest in rooms.values()):
        print("No rooms are currently occupied.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        checkout_room()
    elif choice == "4":
        view_guests()
    elif choice == "5":
        print("Exiting Hotel Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
