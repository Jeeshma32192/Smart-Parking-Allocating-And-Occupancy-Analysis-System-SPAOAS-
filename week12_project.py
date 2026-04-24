from parking import ParkingLot
from storage import load_slots, save_slots, save_log, load_logs
from analytics import occupancy_stats, generate_reports
from charts import plot_status_chart, plot_type_chart, plot_occupancy_trend
from datetime import datetime

parking_lot = ParkingLot()

try:
    parking_lot.slots = load_slots()
except Exception:
    print("Error loading data")

while True:
    print("\nSMART PARKING SYSTEM")
    print("1. Add Parking Slot")
    print("2. View All Slots")
    print("3. Update Slot Status")
    print("4. Allocate Slot")
    print("5. View Analytics (NumPy)")
    print("6. Generate Reports (Pandas)")
    print("7. Show Charts")
    print("8. Exit")

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

            status = input("Enter Slot Status (Free / Occupied): ")
            if status.lower() not in ["free", "occupied"]:
                print("Invalid Status")
                continue

            parking_lot.add_slot(slot_id, slot_type, status)
            save_slots(parking_lot.slots)
            print("Slot added successfully")

        except ValueError:
            print("Invalid input")

    elif choice == "2":
        parking_lot.view_slots()

    elif choice == "3":
        try:
            slot_id = int(input("Enter Slot ID: "))
            status = input("Enter New Status (Free / Occupied): ")

            if status.lower() not in ["free", "occupied"]:
                print("Invalid Status")
                continue

            parking_lot.update_slot_status(slot_id, status)
            save_slots(parking_lot.slots)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_log((slot_id, status, timestamp))

        except ValueError:
            print("Invalid input")

    elif choice == "4":
        slot_type = input("Enter Slot Type Required: ")
        if slot_type.lower() not in ["regular", "ev", "accessible"]:
            print("Invalid Slot Type")
            continue

        parking_lot.allocate_slot(slot_type)
        save_slots(parking_lot.slots)

    elif choice == "5":
        occupancy_stats(parking_lot.slots)

    elif choice == "6":
        generate_reports(parking_lot.slots)

    elif choice == "7":
        logs = load_logs()
        plot_status_chart(parking_lot.slots)
        plot_type_chart(parking_lot.slots)
        plot_occupancy_trend(logs)

    elif choice == "8":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
