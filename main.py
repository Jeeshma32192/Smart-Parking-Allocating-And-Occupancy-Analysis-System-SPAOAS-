import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class Slot:
    def __init__(self, slot_id, slot_type, status="Free"):
        self.id = int(slot_id)
        self.type = slot_type
        self.status = status

class ParkingLot:
    def __init__(self):
        self.slots = []
        self.logs = []
        self.load_data()

    def add_slot(self):
        sid = int(input("Enter Slot ID: "))
        stype = input("Enter Slot Type: ")
        self.slots.append(Slot(sid, stype))
        print("Slot added")

    def view_slots(self):
        if not self.slots:
            print("No slots available")
            return
        print("\nID\tTYPE\tSTATUS")
        for s in self.slots:
            print(f"{s.id}\t{s.type}\t{s.status}")

    def update_slot(self):
        sid = int(input("Enter Slot ID: "))
        for s in self.slots:
            if s.id == sid:
                new_status = input("Enter Status (Free/Occupied): ")
                s.status = new_status
                self.logs.append((sid, new_status, datetime.now()))
                print("Updated")
                return
        print("Slot not found")

    def allocate_slot(self):
        stype = input("Enter Slot Type: ")
        for s in self.slots:
            if s.type.lower() == stype.lower() and s.status == "Free":
                s.status = "Occupied"
                self.logs.append((s.id, "Occupied", datetime.now()))
                print("Allocated Slot:", s.id)
                return
        print("No slot available")

    def analytics(self):
        total = len(self.slots)
        occupied = sum(1 for s in self.slots if s.status == "Occupied")
        free = total - occupied
        print("\nTotal:", total)
        print("Occupied:", occupied)
        print("Free:", free)

    def reports(self):
        if not self.slots:
            print("No data")
            return
        df = pd.DataFrame([(s.id, s.type, s.status) for s in self.slots],
                          columns=["ID", "Type", "Status"])
        print(df.groupby("Type").count())

    def charts(self):
        if not self.slots:
            print("No data")
            return

        status = [s.status for s in self.slots]
        types = [s.type for s in self.slots]

        pd.Series(status).value_counts().plot(kind="bar")
        plt.title("Status")
        plt.show()

        pd.Series(types).value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Types")
        plt.ylabel("")
        plt.show()

    def save_data(self):
        with open("slots.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "type", "status"])
            for s in self.slots:
                writer.writerow([s.id, s.type, s.status])

        with open("logs.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "status", "time"])
            for log in self.logs:
                writer.writerow(log)

    def load_data(self):
        try:
            with open("slots.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.slots.append(Slot(row["id"], row["type"], row["status"]))
        except:
            pass

        try:
            with open("logs.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.logs.append((row["id"], row["status"], row["time"]))
        except:
            pass

def menu():
    p = ParkingLot()
    while True:
        print("\nSMART PARKING SYSTEM")
        print("1. Add Slot")
        print("2. View Slots")
        print("3. Update Slot")
        print("4. Allocate Slot")
        print("5. Analytics")
        print("6. Reports")
        print("7. Charts")
        print("8. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            p.add_slot()
        elif ch == "2":
            p.view_slots()
        elif ch == "3":
            p.update_slot()
        elif ch == "4":
            p.allocate_slot()
        elif ch == "5":
            p.analytics()
        elif ch == "6":
            p.reports()
        elif ch == "7":
            p.charts()
        elif ch == "8":
            p.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()
