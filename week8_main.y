from parking import ParkingLot
from storage import load_slots, save_slots, save_log
from datetime import datetime

parking_lot = ParkingLot()

try:
    parking_lot.slots = load_slots()
except Exception:
    print("Error loading slot data")

while True:
    print("\nSMART PARKING MENU")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Update Slot Status")
    print("4. Allocate Slot")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            slot_id = int(input("Enter Slot ID: "))
            if slot_id <= 0:
                print("Invalid Slot ID")
                continue

            slot_type = input("Enter Slot Type (Regular / EV / Accessible): ")
            if slot_type.lower() not in ["regular", "ev", "accessible"]:
                print("Invalid Slot Type")
                continue

            slot_status = input("Enter Slot Status (Free / Occupied): ")
            if slot_status.lower() not in ["free", "occupied"]:
                print("Invalid Slot Status")
                continue

            parking_lot.add_slot(slot_id, slot_type, slot_status)
            save_slots(parking_lot.slots)

            print("Slot added successfully")

        except ValueError:
            print("Invalid input")

    elif choice == "2":
        parking_lot.view_slots()

    elif choice == "3":
        try:
            slot_id = int(input("Enter Slot ID to update: "))
            new_status = input("Enter New Status (Free / Occupied): ")

            if new_status.lower() not in ["free", "occupied"]:
                print("Invalid Status")
                continue

            parking_lot.update_slot_status(slot_id, new_status)
            save_slots(parking_lot.slots)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_log((slot_id, new_status, timestamp))

        except ValueError:
            print("Invalid input")

    elif choice == "4":
        try:
            slot_type = input("Enter Slot Type Required: ")

            if slot_type.lower() not in ["regular", "ev", "accessible"]:
                print("Invalid Slot Type")
                continue

            parking_lot.allocate_slot(slot_type)
            save_slots(parking_lot.slots)

        except Exception:
            print("Error during allocation")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
