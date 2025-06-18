# from subject import subject
subjects = ["English", "Maths", "Physics", "Chemistry", "Commerce", "Economics", "Literature"]
# chosen_subjects = subject(subjects)
def subject(subjects):
    """
    Function to display and return the list of subjects.
    """
    print("\nAvailable subjects:")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")
        pass
    
    selected_subjects = input("Select your subjects by entering their numbers separated by commas: ")
    selected_indices = [int(i.strip()) - 1 for i in selected_subjects.split(",") if i.strip().isdigit() and 0 <= int(i.strip()) - 1 < len(subjects)]
    
    if not selected_indices:
        print("No valid subjects selected. Please try again.")
        return subject(subjects)
    
    chosen_subjects = [subjects[i] for i in selected_indices]
    print(f"You have chosen: {', '.join(chosen_subjects)}")
    
    return chosen_subjects

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
        "personal_phone": personal_phone,
        # "subject": chosen_subjects
    }

    students.append(student)
    print(f"\nStudent {full_name} added successfully!\n")