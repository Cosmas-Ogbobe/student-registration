# from subject import subject
from contacts import contacts
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
    if age < 5 or age > 100:
        print("Age must be between 5 and 100.")
        return
    
    
    guardian_email, personal_email,guardian_phone = contacts(students)
    if guardian_email is None or personal_email is None:
        return  # Abort if email input failed
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