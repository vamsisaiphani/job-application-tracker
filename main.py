import datetime

def add_application():
    company = input("Company name: ").strip()
    role = input("Role applied for: ").strip()

    if not company or not role:
        print("Company and role cannot be empty.")
        return

    status = input("Status (Applied / Interview / Rejected): ").strip()
    notes = input("Notes (optional): ").strip()
    date_applied = datetime.date.today().isoformat()

    record = f"{company},{role},{date_applied},{status},{notes}\n"

    with open("data/applications.csv", "a") as file:
        file.write(record)

    print("✅ Application saved")

def view_applications():
    try:
        with open("data/applications.csv", "r") as file:
            print("\n--- Job Applications ---")
            print(file.read())
    except FileNotFoundError:
        print("No applications found.")

def main():
    print("\nJob Application Tracker")
    print("1. Add application")
    print("2. View applications")

    choice = input("Enter choice: ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
