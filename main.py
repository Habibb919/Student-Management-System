def add_student(students):
    name = input("Student name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Student name: ").strip()

    while True:
        try:
            grade = float(input("Student grade: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= grade <= 100:
            break

        print("Grade must be between 0 and 100.")

    students.append({"name": name, "grade": grade})
    print("\nStudent added successfully!")


def view_students(students):
    if not students:
        print("No students to display.")
        return

    print("\nStudents:")
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']} - {student['grade']:g}")


def calculate_average(students):
    if not students:
        print("No students available to calculate the average.")
        return

    total = 0
    for student in students:
        total += student["grade"]

    average = total / len(students)
    print(f"Average grade: {average:.2f}")


def find_highest_grade(students):
    if not students:
        print("No students available.")
        return

    highest = students[0]["grade"]
    for student in students:
        if student["grade"] > highest:
            highest = student["grade"]

    print(f"Highest grade: {highest:g}")
    print("Student(s) with the highest grade:")
    for student in students:
        if student["grade"] == highest:
            print(student["name"])


def main():
    students = []

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. View students")
        print("3. Calculate average")
        print("4. Highest grade")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            find_highest_grade(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")


main()