class Slot:
    def __init__(self, slot_id, slot_type, status):
        self.id = slot_id
        self.type = slot_type
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display_slot(self):
        print(f"{self.id:<10}{self.type:<15}{self.status:<10}")


class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot_id, slot_type, status):
        slot = Slot(slot_id, slot_type, status)
        self.slots.append(slot)

    def view_slots(self):
        if not self.slots:
            print("No parking slots available")
        else:
            print("\nID        TYPE           STATUS")
            print("-----------------------------------")
            for slot in self.slots:
                slot.display_slot()

    def update_slot_status(self, slot_id, new_status):
        for slot in self.slots:
            if slot.id == slot_id:
                slot.update_status(new_status)
                print("Slot status updated")
                return
        print("Slot not found")

    def allocate_slot(self, slot_type):
        for slot in self.slots:
            if slot.type.lower() == slot_type.lower() and slot.status.lower() == "free":
                slot.update_status("Occupied")
                print(f"Allocated Slot ID: {slot.id}")
                return
        print("No available slot found")
