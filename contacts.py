def contacts(students):
    counter = 0
    guardian_email = ""

    while counter < 3:
        guardian_email = input("Enter your guardian email: ").lower().strip()
        
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
        return None, None, None  # Consistently return 3 values

    personal_email = input("Enter your personal email: ").lower().strip()

    if not personal_email:
        print("Personal email is compulsory.")
        return None, None, None
    elif personal_email == guardian_email:
        print("Personal email cannot be the same as guardian email.")
        return None, None, None

    while True:
        guardian_phone = input("Enter your guardian phone (compulsory): ").strip()

        if not guardian_phone:
            print("Guardian phone is compulsory.")
        elif not (guardian_phone.startswith("+") or guardian_phone.startswith("0")):
            print("Guardian phone must start with '+' or '0'.")
        elif not guardian_phone.replace("+", "").isdigit():
            print("Guardian phone must be numeric.")
        elif len(guardian_phone.replace("+", "")) < 10 or len(guardian_phone.replace("+", "")) > 15:
            print("Guardian phone must be between 10 and 15 digits.")
        else:
            print(f"Guardian phone: {guardian_phone} is valid.")
            break

    
    return guardian_email, personal_email, guardian_phone
