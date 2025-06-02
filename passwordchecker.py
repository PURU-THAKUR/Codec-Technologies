import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        strength = "Strong 💪"
    elif 3 <= score < 5:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"










    print(f"Password Strength: {strength}")
    if length_error:
        print("- Minimum 8 characters required.")
    if digit_error:
        print("- Add at least one digit.")
    if uppercase_error:
        print("- Add at least one uppercase letter.")
    if lowercase_error:
        print("- Add at least one lowercase letter.")
    if symbol_error:
        print("- Add at least one special character.")

# Example usage:
password = input("Enter your password to check: ")
check_password_strength(password)
# Example usage:
password = input("Enter your password to check: ")
check_password_strength(password)

input("Press Enter to exit...")
