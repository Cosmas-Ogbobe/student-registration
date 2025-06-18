def print_student_details(students):
    print("Student Details:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Address: {student.get('address', 'N/A')}")
        print(f"Guardian Phone: {student['phones'].get('guardian', 'N/A')}")
        print("Personal Phones:")
        for phone in student["phones"].get("personal", []):
            print(f"  - {phone}")
        print("Emails:")
        for email in student.get('emails', []):
            print(f"  - {email}")
        print("Subjects:")
        for i, subject in enumerate(student.get('subjects', []), start=1):
            print(f"  {i}. {subject}")
        # print()  # Blank line between students

# Example call:
# print_student_details(students)
