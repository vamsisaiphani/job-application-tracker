import datetime

DATA_FILE = "data/applications.csv"
VALID_STATUSES = ["Applied", "Interview", "Rejected"]


def read_applications():
    try:
        with open(DATA_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_applications(lines):
    with open(DATA_FILE, "w") as file:
        file.writelines(lines)


def add_application():
    company = input("Company name: ").strip()
    role = input("Role applied for: ").strip()

    if not company or not role:
        print("Company and role cannot be empty.")
        return

    status = input("Status (Applied / Interview / Rejected): ").strip()
    if status not in VALID_STATUSES:
        print("Invalid status.")
        return

    notes = input("Notes (optional): ").strip()
    date_applied = datetime.date.today().isoformat()

    record = f"{company},{role},{date_applied},{status},{notes}\n"

    with open(DATA_FILE, "a") as file:
        file.write(record)

    print("✅ Application saved")


def view_applications():
    lines = read_applications()
    if not lines:
        print("No applications found.")
        return

    print("\n--- Job Applications ---")
    for line in lines:
        print(line.strip())


def update_status():
    lines = read_applications()
    if not lines:
        print("No applications to update.")
        return

    for index, line in enumerate(lines):
        company, role, date, status, notes = line.strip().split(",")
        print(f"{index + 1}. {company} - {role} [{status}]")

    try:
        choice = int(input("Select application number to update: ")) - 1
        if choice < 0 or choice >= len(lines):
            print("Invalid selection.")
            return

        new_status = input("Enter new status (Applied / Interview / Rejected): ").strip()
        if new_status not in VALID_STATUSES:
            print("Invalid status.")
            return

        parts = lines[choice].strip().split(",")
        parts[3] = new_status
        lines[choice] = ",".join(parts) + "\n"

        write_applications(lines)
        print("✅ Status updated successfully")

    except ValueError:
        print("Invalid input.")


def filter_by_status():
    status_filter = input("Enter status to filter (Applied / Interview / Rejected): ").strip()
    if status_filter not in VALID_STATUSES:
        print("Invalid status.")
        return

    lines = read_applications()
    if not lines:
        print("No applications found.")
        return

    print(f"\n--- Applications with status: {status_filter} ---")
    found = False

    for line in lines:
        company, role, date, status, notes = line.strip().split(",")
        if status == status_filter:
            print(f"{company} | {role} | {date} | {status} | {notes}")
            found = True

    if not found:
        print("No applications found for this status.")


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
