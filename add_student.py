from subject import subject
subjects = ["English", "Maths", "Physics", "Chemistry", "Commerce", "Economics", "Literature"]

def add_student(students):

    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = f"{first_name} {last_name}".strip()
    age = input("Enter your age: ").isdigit()
    if not age:
        print("Age must be a number.")
        return
    age = int(age)
    guardian_email = input("Enter your guardian email: ")
    personal_email = input("Enter your personal email: ")
    guardian_phone = input("Enter your guardian phone (compulsory): ")
    personal_phone = input("Enter your personal phone (compulsory): ")
    print("\n Chose your subjects from the list below:")
    subject(subjects)    
    student = {
        "name": full_name,
        "age": age,
        "guardian_email": guardian_email,
        "personal_email": personal_email,
        "guardian_phone": guardian_phone,
        "personal_phone": personal_phone
    }

    students.append(student)
    print(f"\nStudent {full_name} added successfully!\n")
