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
    counter = 0
    guardian_email = ""
    while counter < 3:
        guardian_email = input("Enter your guardian email: ")
        if not guardian_email:
            print("Guardian email is compulsory.")
        elif "@" not in guardian_email or "." not in guardian_email:
            print("Invalid guardian email format.")
        else:
            print(f"Guardian email: {guardian_email} is valid.")
            break
        counter += 1
    else:
        print("Too many invalid attempts. Student not added.")
        return

    personal_email = input("Enter your personal email: ")
    guardian_phone = input("Enter your guardian phone (compulsory): ")
    if not guardian_phone:
        print("Guardian phone is compulsory.")
        return
    
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