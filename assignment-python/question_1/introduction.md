## Password Strength Checker

## Question

#### Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password.

- Implement a Python function called `check_password_strength` that takes a password string as input.

- The function should check the password against the following criteria:

  - **Minimum length:** The password should be at least **8 characters** long.
  - **Contains both uppercase and lowercase letters.**
  - **Contains at least one digit (0-9).**
  - **Contains at least one special character** (e.g., `!`, `@`, `#`, `$`, `%`).

- The function should return a **boolean value** indicating whether the password meets the criteria.

- Write a script that takes **user input** for a password and calls the `check_password_strength` function to validate it.

- Provide **appropriate feedback** to the user based on the strength of the password.
---

### Overview
This script validates the strength of a given password based on specific criteria:
- Minimum length of 8 characters
- Contains both uppercase and lowercase letters
- Contains at least one digit (0-9)
- Contains at least one special character

### How to Use
1. Run the script in a Python environment.
 run: ```python question_1.py```
2. Enter a password when prompted.
3. The script will evaluate the password based on the defined criteria.
4. If the password is weak, suggestions for improvement will be displayed.
5. If the password meets all criteria, a confirmation message will be shown.

### Example Output
#### Weak Password Input:
```
Enter your password: pass123
Weak password. Please follow the guidelines:
- Password must contain both uppercase and lowercase letters.
- Password must contain at least one special character (e.g., !, @, #, $, %).
Please try again with a stronger password.
```

#### Strong Password Input:
```
Enter your password: Secure@123
Password is strong.
