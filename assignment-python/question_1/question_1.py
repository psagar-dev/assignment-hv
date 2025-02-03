import re

def check_password_strength(password: str) -> bool:
    """
    Validates the strength of a given password based on:
    - Minimum length of 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit (0-9)
    - Contains at least one special character
    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        errors.append("Password must contain both uppercase and lowercase letters.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit (0-9).")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character (e.g., !, @, #, $, %).")

    if errors:
        print("Weak password. Please follow the guidelines:")
        for error in errors:
            print(f"- {error}")
        return False

    return True

if __name__ == "__main__":
    input_password = input("Enter your password: ")
    if check_password_strength(input_password):
        print("Password is strong.")
    else:
        print("Please try again with a stronger password.")
