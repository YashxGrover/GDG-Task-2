FILE_NAME = "students.txt"

def load_students():
    """Reads all student records from the file into a list of dictionaries."""
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:  
                    continue
                roll, name, marks_str = line.split("|")
                marks = [float(m) for m in marks_str.split(",")]
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": marks
                })
    except FileNotFoundError:
       
        return []
    return students


def add_student():
    """Collects student details, validates marks, and appends to the file."""
    roll = input("Enter roll number: ").strip()
    if not roll:
        print("Roll number cannot be empty.")
        return

    
    existing_students = load_students()
    for s in existing_students:
        if s["roll"] == roll:
            print("A student with this roll number already exists!")
            return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        raw_marks = input("Enter marks separated by spaces (e.g., 85 90 78): ")
        marks = [float(m) for m in raw_marks.split()]
        if not marks:
            print("You must enter at least one mark.")
            return
    except ValueError:
        print("Invalid input! Please enter numbers only for marks.")
        return

    marks_str = ",".join(str(m) for m in marks)
    with open(FILE_NAME, "a") as file:
        file.write(f"{roll}|{name}|{marks_str}\n")

    print(f"Student '{name}' added successfully!")


def view_students():
    """Displays all saved student records in a readable format."""
    students = load_students()
    if not students:
        print("No student records found.")
        return

    print("\n--- All Student Records ---")
    for s in students:
        marks_display = ", ".join(str(m) for m in s["marks"])
        print(f"Roll No: {s['roll']} | Name: {s['name']} | Marks: [{marks_display}]")
    print("---------------------------")


def search_student():
    """Searches for a student by roll number and displays their record."""
    target_roll = input("Enter roll number to search: ").strip()
    students = load_students()

    for s in students:
        if s["roll"] == target_roll:
            marks_display = ", ".join(str(m) for m in s["marks"])
            print(f"\nRecord Found -> Roll No: {s['roll']} | Name: {s['name']} | Marks: [{marks_display}]")
            return

    print("Student not found.")


def calculate_average():
    """Calculates and displays a specific student's average marks."""
    target_roll = input("Enter roll number to calculate average marks: ").strip()
    students = load_students()

    for s in students:
        if s["roll"] == target_roll:
            avg = sum(s["marks"]) / len(s["marks"])
            print(f"Average marks for {s['name']} (Roll {s['roll']}): {avg:.2f}")
            return

    print("Student not found.")


def main():
    """Runs the main menu-driven program loop."""
    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
