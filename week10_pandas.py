import pandas as pd

def generate_reports(slots):
    if not slots:
        print("No parking data available")
        return

    data = {
        "id": [slot.id for slot in slots],
        "type": [slot.type for slot in slots],
        "status": [slot.status for slot in slots]
    }

    df = pd.DataFrame(data)

    print("\nSLOT TYPE USAGE")
    print("-----------------------------------")
    type_usage = df.groupby("type").size()
    print(type_usage)

    print("\nOCCUPANCY STATUS COUNT")
    print("-----------------------------------")
    status_count = df["status"].value_counts()
    print(status_count)
