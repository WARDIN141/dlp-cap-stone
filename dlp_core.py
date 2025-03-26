import re

def ee(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}'
    return re.findall(email_pattern, text)

def epn(text):
    phone_pattern = r'(?:\+91[\s-]?)?(?:91[\s-]?)?[6-9]\d{9}'
    return re.findall(phone_pattern, text)

def eccn(text):
    cc_pattern = r'\b(?:4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}|5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}|3[47]\d{2}[\s-]?\d{6}[\s-]?\d{5})\b'
    return re.findall(cc_pattern, text)

def ep(text):
    pwd_pattern = r'(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}'
    return re.findall(pwd_pattern, text)

def process_file(file_path):
    """Reads the file and extracts sensitive data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        emails = ee(text)
        phone_numbers = epn(text)
        credit_cards = eccn(text)
        passwords = ep(text)

        print("\n--- Detection Report ---")
        if emails:
            print("Emails:", emails)
        if phone_numbers:
            print("Phone Numbers:", phone_numbers)
        if credit_cards:
            print("Credit Card Numbers:", credit_cards)
        if passwords:
            print("Possible Passwords:", passwords)

        if not any([emails, phone_numbers, credit_cards, passwords]):
            print("No sensitive data found.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")


file_path = input("Enter the file path: ").strip().strip('"')
process_file(file_path)
