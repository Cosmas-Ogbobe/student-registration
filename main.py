# Student Management System
from add_student import add_student
from search_student import search_student
from edit_student import edit_student
from users_details import student_details

students = []


while True:
    print("\nStudent Management System")
    # print("Available subjects:", ", ".join(subjects))
    print("Choose an option:")
    print("1. Add student")
    print("2. Search student")
    print("3. Edit student")
    print("#. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Adding a new student...")
        add_student(students)
    elif choice == "2":
        print("Searching for student...")
        # student_details(students)
        search_student(students)
    elif choice == "3":
       edit_student(students)
    elif choice == "#":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")