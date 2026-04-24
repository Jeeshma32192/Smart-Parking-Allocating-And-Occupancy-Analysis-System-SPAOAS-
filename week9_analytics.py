import numpy as np

def occupancy_stats(slots):
    if not slots:
        print("No parking data available")
        return

    statuses = [1 if slot.status.lower() == "occupied" else 0 for slot in slots]
    arr = np.array(statuses)

    total_slots = len(arr)
    occupied = np.sum(arr)
    free = total_slots - occupied
    occupancy_percentage = (occupied / total_slots) * 100

    print("\nPARKING OCCUPANCY STATISTICS")
    print("-----------------------------------")
    print(f"Total Slots       : {total_slots}")
    print(f"Occupied Slots    : {occupied}")
    print(f"Free Slots        : {free}")
    print(f"Occupancy %       : {occupancy_percentage:.2f}")
