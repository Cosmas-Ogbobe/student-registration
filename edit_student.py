def edit_student(students):
    """Edit student details by last name."""
    last_name = input("Enter last name of the student to edit: ").lower()
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
                f"{'Subjects'.ljust(18)}: {', '.join(student.get('subjects', []))}"
            )
            
            # Edit details
            student["name"] = input("Enter new name (or press Enter to keep current): ") or student["name"]
            age_input = input("Enter new age (or press Enter to keep current): ")
            if age_input.isdigit():
                student["age"] = int(age_input)
            guardian_email = input("Enter new guardian email (or press Enter to keep current): ")
            if guardian_email:
                student["guardian_email"] = guardian_email
            personal_email = input("Enter new personal email (or press Enter to keep current): ")
            if personal_email:
                student["personal_email"] = personal_email
            guardian_phone = input("Enter new guardian phone (or press Enter to keep current): ")
            if guardian_phone:
                student["guardian_phone"] = guardian_phone
            personal_phone = input("Enter new personal phone (or press Enter to keep current): ")
            if personal_phone:
                student["personal_phone"] = personal_phone
            
            print(f"\nStudent {full_name} updated successfully!\n")
            return student
    
    print("Student not found.")
    return None