# PROG103 Assignment 1
# Student Record Management System
# Terminal Based Application

PASS_MARK = 50
students = []


# Function to calculate average marks
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average


# Function to determine grade
def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


# Function to add student record
def add_student():
    print("\n--- Add Student Record ---")

    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")

    mark1 = float(input("Enter Programming Mark: "))
    mark2 = float(input("Enter Networking Mark: "))
    mark3 = float(input("Enter Database Mark: "))

    average = calculate_average(mark1, mark2, mark3)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "id": student_id,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent record added successfully.")


# Function to display all students
def display_students():

    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No records available.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Student ID:", student["id"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("-------------------------")


# Function to search for a student
def search_student():

    search_id = input("\nEnter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:

            print("\nStudent Found")
            print("Name:", student["name"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            return

    print("Student not found.")


# Main menu function
def menu():

    while True:

        print("\n===== Student Record Management System =====")
        print("1. Add Student Record")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()
