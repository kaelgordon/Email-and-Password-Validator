# Email-and-Password-Validator
# Mini Email & Password Validator

This is a simple Python project that validates user-provided email addresses and passwords according to real-world rules.  

It was created as part of beginner Python practice and demonstrates the use of loops, flags, string methods, and conditional logic.

---

## **Features**

### Email Validation
- Must contain `@` and `.`  
- Must contain exactly **one** `@`  
- Cannot contain spaces  
- Must be at least **5 characters long**

### Password Validation
- Must be at least **8 characters long**  
- Must contain at least **one uppercase letter**  
- Must contain at least **one lowercase letter**  
- Must contain at least **one digit**  
- Cannot contain spaces  
- Cannot be identical to the email  
- Must start and end with a **letter or digit**

---

## **Usage**

1. Clone or download the repository.
2. Run the script with Python 3:

Enter your email: test@domain.com
Enter your password: MyPass123

✅ Email and password are valid!
Enter your email: test@@domain.com
Enter your password: pass

❌ Email errors:
- Email must contain exactly one '@'
❌ Password errors:
- Password must be at least 8 characters long
- Password must contain at least one uppercase letter
- Password must contain at least one digit
```bash
python validator.py
