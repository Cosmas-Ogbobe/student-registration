def search_student(students):
    last_name = input("Enter last name of the student to search: ").lower()
    for student in students:
        full_name = student["name"]
        name_parts = full_name.strip().split()
        if name_parts and name_parts[-1].lower() == last_name:
            print("Student found. Details below")
            print(
                f"{'Name'.ljust(18)}: {student['name']}\n"
                f"{'Age'.ljust(18)}: {student['age']}\n"
                f"{'Guardian Email'.ljust(18)}: {student['guardian_email']}\n"
                f"{'Personal Email'.ljust(18)}: {student['personal_email']}\n"
                f"{'Guardian Phone'.ljust(18)}: {student['guardian_phone']}\n"
                f"{'Personal Phone'.ljust(18)}: {student['personal_phone']}\n"
                f"{'Subjects'.ljust(18)}: {', '.join(student.get('chosen_subjects', []))}"
        )

            return student
    print("Student not found.")
    return None
