from datetime import datetime

parking_slots = []
logs = []
slot_types = {"Regular", "EV", "Accessible"}

def add_slot():
    try:
        slot_id = int(input("Enter Slot ID: "))
        if slot_id <= 0:
            print("Invalid Slot ID")
            return

        slot_type = input("Enter Slot Type (Regular / EV / Accessible): ")
        if slot_type not in slot_types:
            print("Invalid Slot Type")
            return

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


def update_slot_status():
    try:
        slot_id = int(input("Enter Slot ID to update: "))
        for slot in parking_slots:
            if slot["id"] == slot_id:
                new_status = input("Enter New Status (Free / Occupied): ")
                slot["status"] = new_status

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log = (slot_id, new_status, timestamp)
                logs.append(log)

                print("Slot status updated")
                return

        print("Slot not found")

    except ValueError:
        print("Invalid input")


def view_logs():
    if not logs:
        print("No logs available")
    else:
        print("\nSLOT ID   STATUS      TIMESTAMP")
        print("---------------------------------------------")
        for log in logs:
            print(f"{log[0]:<10}{log[1]:<12}{log[2]}")


while True:
    print("\nSMART PARKING MENU")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Update Slot Status")
    print("4. View Logs")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_slot()
    elif choice == "2":
        view_slots()
    elif choice == "3":
        update_slot_status()
    elif choice == "4":
        view_logs()
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
