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

def update_status():
    try:
        with open("data/applications.csv", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No applications to update.")
            return

        for index, line in enumerate(lines):
            company, role, date, status, notes = line.strip().split(",")
            print(f"{index + 1}. {company} - {role} [{status}]")

        choice = int(input("Select application number to update: ")) - 1

        if choice < 0 or choice >= len(lines):
            print("Invalid selection.")
            return

        new_status = input("Enter new status (Applied / Interview / Rejected): ").strip()
        parts = lines[choice].strip().split(",")
        parts[3] = new_status
        lines[choice] = ",".join(parts) + "\n"

        with open("data/applications.csv", "w") as file:
            file.writelines(lines)

        print("✅ Status updated successfully")

    except FileNotFoundError:
        print("No applications found.")
    except ValueError:
        print("Invalid input.")

def main():
    print("\nJob Application Tracker")
    print("1. Add application")
    print("2. View applications")
    print("3. Update application status")
    print("4. Filter applications by status")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        update_status()
    elif choice == "4":
        filter_by_status()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
