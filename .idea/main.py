from student import Student
from utils.data_utils import save_data, load_data
from utils.email_utils import send_email

students = load_data()

def add_student():
    name = input("Enter student name: ")
    rate = float(input("Enter fees rate per class: "))
    students[name] = Student(name, rate)
    save_data(students)
    print(f"Student {name} added.")

def mark_attendance():
    name = input("Enter student name: ")
    date = input("Enter date attended (YYYY-MM-DD): ")
    if name in students:
        students[name].add_attendance(date)
        save_data(students)
        print(f"Attendance marked for {name} on {date}.")
    else:
        print("Student not found!")

def record_payment():
    name = input("Enter student name: ")
    amount = float(input("Enter amount paid: "))
    expected_classes = int(input("How many classes did they intend to pay for this month? "))
    if name in students:
        students[name].pay_fees(amount, expected_classes)
        save_data(students)
        print(f"Payment of ${amount} recorded for {name}.")
    else:
        print("Student not found!")

def show_summary():
    name = input("Enter student name to show summary: ")
    if name in students:
        student = students[name]
        due = student.calculate_due()
        print(f"\nSummary for {student.name}:")
        print(f"Dates attended: {student.dates_attended}")
        print(f"Fees paid: ${student.fees_paid}")
        print(f"Remaining due: ${due}")
        print(f"Credit classes: {student.credit_classes}")
    else:
        print("Student not found!")

def send_monthly_summary():
    from_email = input("Your email address: ")
    password = input("Your email password (or app password): ")

    for student in students.values():
        due = student.calculate_due()
        body = (
            f"Hello,\n\n"
            f"This is your monthly summary for {student.name}.\n"
            f"Dates attended: {', '.join(student.dates_attended)}\n"
            f"Fees paid: ${student.fees_paid}\n"
            f"Credit classes available: {student.credit_classes}\n"
            f"Remaining due: ${due}\n\n"
            f"Thank you!"
        )
        parent_email = input(f"Enter email of {student.name}'s parent: ")
        send_email(parent_email, f"{student.name} Monthly Fee Summary", body, from_email, password)
        print(f"Summary email sent to {parent_email}")

def menu():
    while True:
        print("\nAttendance & Fees Tracker")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Record payment")
        print("4. Show student summary")
        print("5. Send monthly summary emails")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            record_payment()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            send_monthly_summary()
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
