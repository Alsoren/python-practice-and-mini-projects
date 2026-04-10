import re 

def is_valid_email(email):
    pattern = r"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern,email)

while True:
    email = input("Enter your email address: ")
    if is_valid_email(email):
        print(f"Thanks, your email address: {email}")
        break
    else:
        print("please enter a valid email address.")
