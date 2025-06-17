
def subject(subjects):
    """
    Function to display and return the list of subjects.
    """
    print("\nAvailable subjects:")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")
    
    selected_subjects = input("Select your subjects by entering their numbers separated by commas: ")
    selected_indices = [int(i.strip()) - 1 for i in selected_subjects.split(",") if i.strip().isdigit() and 0 <= int(i.strip()) - 1 < len(subjects)]
    
    if not selected_indices:
        print("No valid subjects selected. Please try again.")
        return subject(subjects)
    
    chosen_subjects = [subjects[i] for i in selected_indices]
    print(f"You have chosen: {', '.join(chosen_subjects)}")
    
    return chosen_subjects