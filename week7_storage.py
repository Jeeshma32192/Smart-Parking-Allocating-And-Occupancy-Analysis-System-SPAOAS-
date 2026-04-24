import csv
import os
from parking import Slot

SLOTS_FILE = "slots.csv"
LOGS_FILE = "logs.csv"


def save_slots(slots):
    with open(SLOTS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "type", "status"])
        for slot in slots:
            writer.writerow([slot.id, slot.type, slot.status])


def load_slots():
    slots = []
    if not os.path.exists(SLOTS_FILE):
        return slots

    with open(SLOTS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            slot = Slot(int(row["id"]), row["type"], row["status"])
            slots.append(slot)

    return slots


def save_log(log):
    file_exists = os.path.exists(LOGS_FILE)

    with open(LOGS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["slot_id", "status", "timestamp"])

        writer.writerow(log)


def load_logs():
    logs = []
    if not os.path.exists(LOGS_FILE):
        return logs

    with open(LOGS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            logs.append((row["slot_id"], row["status"], row["timestamp"]))

    return logs
