parking_slots = []

while True:
    print("\nSMART PARKING MENU")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Search by Slot ID")
    print("4. Search by Slot Type")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            slot_id = int(input("Enter Slot ID: "))
            if slot_id <= 0:
                print("Invalid Slot ID")
                continue

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

    elif choice == "2":
        if not parking_slots:
            print("No parking slots available")
        else:
            print("\nID        TYPE           STATUS")
            print("-----------------------------------")
            for slot in parking_slots:
                print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")

    elif choice == "3":
        try:
            search_id = int(input("Enter Slot ID to search: "))
            found = False

            for slot in parking_slots:
                if slot["id"] == search_id:
                    print("\nID        TYPE           STATUS")
                    print("-----------------------------------")
                    print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")
                    found = True
                    break

            if not found:
                print("Slot not found")

        except ValueError:
            print("Invalid input")

    elif choice == "4":
        search_type = input("Enter Slot Type to search: ").lower()
        found = False

        print("\nID        TYPE           STATUS")
        print("-----------------------------------")

        for slot in parking_slots:
            if slot["type"].lower() == search_type:
                print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")
                found = True

        if not found:
            print("No matching slots found")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
