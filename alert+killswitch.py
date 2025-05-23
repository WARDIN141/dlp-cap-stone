import re
import sys

def rf(file_path):
    with open(file_path,'r', encoding='utf-8') as file:
        return file.read()

def ee(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}'
    return re.findall(email_pattern,text)

def epn(text):
    phone_pattern = r'(?:\+91[\s-]?)?(?:91[\s-]?)?[6-9]\d{9}'
    return re.findall( phone_pattern,text)

def eccn(text):
    cc_pattern = r'\b(?:4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}|5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}|3[47]\d{2}[\s-]?\d{6}[\s-]?\d{5})\b'
    return re.findall(cc_pattern,text)

def ep(text):
    pwd_pattern = r'(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}'
    return re.findall(pwd_pattern,text)


def popup(d_category,detection):
    print("ALERT: Sensitive Data Found")
    print(f"{d_category} detected: {detection}")
    print("killswitch activated ,program wont process any further")
    sys.exit(1)

def ptf(file_path):
    text = rf(file_path)

    df={
        "emails": ee,
        "Phone no.s": epn,
        "Credit Card no.": eccn,
        "passwords": ep
        }

    for category, function in df.items():
        detection=function(text)
        if detection:
            popup(category,detection[0])
        else:
            print("no sensitive data found")


file_path = input("Enter the file path: ").strip().strip('"')
ptf(file_path)
            
            
