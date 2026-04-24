import matplotlib.pyplot as plt
import pandas as pd


def plot_status_chart(slots):
    if not slots:
        print("No data available")
        return

    data = [slot.status for slot in slots]
    df = pd.DataFrame(data, columns=["status"])
    counts = df["status"].value_counts()

    plt.figure()
    counts.plot(kind="bar")
    plt.title("Free vs Occupied Slots")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()


def plot_type_chart(slots):
    if not slots:
        print("No data available")
        return

    data = [slot.type for slot in slots]
    df = pd.DataFrame(data, columns=["type"])
    counts = df["type"].value_counts()

    plt.figure()
    counts.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title("Slot Type Distribution")
    plt.show()


def plot_occupancy_trend(logs):
    if not logs:
        print("No log data available")
        return

    df = pd.DataFrame(logs, columns=["slot_id", "status", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    trend = df.groupby("timestamp").size()

    plt.figure()
    trend.plot(kind="line")
    plt.title("Occupancy Trend Over Time")
    plt.xlabel("Time")
    plt.ylabel("Updates Count")
    plt.show()
