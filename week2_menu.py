# WEEK 2 – Menu Driven Parking System
parking_slots = []

while True:
    print("\n===== SMART PARKING MENU =====")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            slot_id = int(input("Enter Slot ID: "))
            
            if slot_id <= 0:
                print("Slot ID must be greater than 0!")
                continue

            slot_type = input("Enter Slot Type (Regular / EV / Accessible): ")
            slot_status = input("Enter Slot Status (Free / Occupied): ")

            slot = {
                "id": slot_id,
                "type": slot_type,
                "status": slot_status
            }

            parking_slots.append(slot)
            print("Slot added successfully!")

        except ValueError:
            print(" Invalid input! Please enter correct data.")

    elif choice == "2":
        if not parking_slots:
            print(" No parking slots available.")
        else:
            print("\n--- Parking Slots ---")
            print(f"{'ID':<10}{'TYPE':<15}{'STATUS':<10}")
            print("-" * 35)

            for slot in parking_slots:
                print(f"{slot['id']:<10}{slot['type']:<15}{slot['status']:<10}")

    elif choice == "3":
        print(" Exiting program...")
        break

    else:
        print(" Invalid choice! Try again.")
