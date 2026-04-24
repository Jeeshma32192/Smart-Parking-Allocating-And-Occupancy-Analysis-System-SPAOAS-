parking_slots = []

def add_slot():
    try:
        slot_id = int(input("Enter Slot ID: "))
        if slot_id <= 0:
            print("Invalid Slot ID")
            return

        slot_type = input("Enter Slot Type (Regular / EV / Accessible): ")
        slot_status = input("Enter Slot Status (Free / Occupied): ")

        slot = {
            "id": slot_id,
            "type": slot_type,
            "status": slot_status
        }

        parking_slots.append(slot)
        print("Slot added successfully")

    except ValueError:
        print("Invalid input")


def view_slots():
    if not parking_slots:
        print("No parking slots available")
    else:
        print("\nID        TYPE           STATUS")
        print("-----------------------------------")
        for slot in parking_slots:
            print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")


def search_slot():
    print("\n1. Search by ID")
    print("2. Search by Type")
    choice = input("Enter choice: ")

    if choice == "1":
        try:
            search_id = int(input("Enter Slot ID: "))
            for slot in parking_slots:
                if slot["id"] == search_id:
                    print("\nID        TYPE           STATUS")
                    print("-----------------------------------")
                    print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")
                    return
            print("Slot not found")
        except ValueError:
            print("Invalid input")

    elif choice == "2":
        search_type = input("Enter Slot Type: ").lower()
        found = False

        print("\nID        TYPE           STATUS")
        print("-----------------------------------")

        for slot in parking_slots:
            if slot["type"].lower() == search_type:
                print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")
                found = True

        if not found:
            print("No matching slots found")

    else:
        print("Invalid choice")


def update_slot_status():
    try:
        slot_id = int(input("Enter Slot ID to update: "))
        for slot in parking_slots:
            if slot["id"] == slot_id:
                new_status = input("Enter New Status (Free / Occupied): ")
                slot["status"] = new_status
                print("Slot status updated")
                return
        print("Slot not found")
    except ValueError:
        print("Invalid input")


while True:
    print("\nSMART PARKING MENU")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Search Slot")
    print("4. Update Slot Status")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_slot()
    elif choice == "2":
        view_slots()
    elif choice == "3":
        search_slot()
    elif choice == "4":
        update_slot_status()
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
