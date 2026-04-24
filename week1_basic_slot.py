# WEEK 1 – Basic Parking Slot Entry Script

slot_id = int(input("Enter Slot ID: "))
slot_type = input("Enter Slot Type (Regular / EV / Accessible): ")
slot_status = input("Enter Slot Status (Free / Occupied): ")

if slot_id <= 0:
    print(" Invalid Slot ID! It must be greater than 0.")
else: 
    print("\n--- Parking Slot Details ---")
    print(f"Slot ID      : {slot_id}")
    print(f"Slot Type    : {slot_type}")
    print(f"Slot Status  : {slot_status}")
