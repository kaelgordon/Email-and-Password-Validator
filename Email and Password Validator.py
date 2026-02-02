def validate_email(email):
    """Check email rules and return a list of errors"""
    errors = []

    if "@" not in email:
        errors.append("Email must contain '@'")
    if "." not in email:
        errors.append("Email must contain '.'")
    if email.count("@") != 1:
        errors.append("Email must contain exactly one '@'")
    if " " in email:
        errors.append("Email cannot contain spaces")
    if len(email) < 5:
        errors.append("Email must be at least 5 characters long")

    return errors


def validate_password(password, email):
    """Check password rules and return a list of errors"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    has_upper = has_lower = has_digit = False
    for c in password:
        if "A" <= c <= "Z":
            has_upper = True
        if "a" <= c <= "z":
            has_lower = True
        if "0" <= c <= "9":
            has_digit = True

    if not has_upper:
        errors.append("Password must contain at least one uppercase letter")
    if not has_lower:
        errors.append("Password must contain at least one lowercase letter")
    if not has_digit:
        errors.append("Password must contain at least one digit")
    if " " in password:
        errors.append("Password cannot contain spaces")
    if password == email:
        errors.append("Password cannot be identical to the email")
    if not (password[0].isalnum() and password[-1].isalnum()):
        errors.append("Password must start and end with a letter or digit")

    return errors


def main():
    """Run the validator project"""
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    email_errors = validate_email(email)
    password_errors = validate_password(password, email)

    if not email_errors and not password_errors:
        print("✅ Email and password are valid!")
    else:
        if email_errors:
            print("\n❌ Email errors:")
            for err in email_errors:
                print(f"- {err}")
        if password_errors:
            print("\n❌ Password errors:")
            for err in password_errors:
                print(f"- {err}")


if __name__ == "__main__":
    main()
