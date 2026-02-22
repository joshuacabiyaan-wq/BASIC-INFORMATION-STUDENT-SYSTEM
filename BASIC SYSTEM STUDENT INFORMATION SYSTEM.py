
# Student Information Management System (Basic)

students = []

def add_student():
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID:")
    full_name = input("Enter Full Name:")
    course = input("Enter Course:")
    year_level = input("Enter Year Level:")
    age = input("Enter Age:")

    student = {
        "Student ID": student_id,
        "Full Name": full_name,
        "Course": course,
        "Year Level": year_level,
        "Age": age
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    print("\n--- Student List ---")
    if len(students) == 0:
        print("No students found.\n")
    else:
        for student in students:
            print(student)
        print()


def search_student():
    print("\n--- Search Student ---")
    search_value = input("Enter Student ID or Full Name: ")

    found = False
    for student in students:
        if student["Student ID"] == search_value or student["Full Name"].lower() == search_value.lower():
            print("Student Found:")
            print(student)
            found = True

    if not found:
        print("Student not found.\n")


def update_student():
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["Student ID"] == student_id:
            print("Leave blank if no change.")
            course = input("New Course: ")
            year_level = input("New Year Level: ")
            age = input("New Age: ")

            if course:
                student["Course"] = course
            if year_level:
                student["Year Level"] = year_level
            if age:
                student["Age"] = age

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["Student ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def main():
    while True:
        print(" ========================================")
        print(" STUDENT INFORMATION MANAGEMENT SYSTEM ")
        print(" ========================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Run the program
main()