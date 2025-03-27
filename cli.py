import re
import sys
import logging
import argparse
from datetime import datetime

logging.basicConfig(
    filename = "C:\\Users\\ANANT\\Desktop\\internship stuff\\data loss provention module\\logger_test.txt",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    force = True
)


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

def lgd(d_category,detection):
    log_message= f"{d_category} detected:{detection}"
    logging.info(log_message)
    
def popup(d_category,detection):
    print("ALERT: Sensitive Data Found")
    print(f"{d_category} detected: {detection}")
    print("killswitch activated ,program wont process any further")
    sys.exit(1)

def ptf(file_path, verbose=False):
    text = rf(file_path)

    df = {
        "Emails": ee,
        "Phone Numbers": epn,
        "Credit Card Numbers": eccn,
        "Passwords": ep
    }

    if verbose:
        print(f"[INFO] Scanning file: {file_path}")

    for category, function in df.items():
        detection = function(text)

        if detection:
            lgd(category, detection[0])

            if verbose:
                print(f"[DETECTED] {category}: {detection}")

            popup(category, detection[0])
        else:
            if verbose:
                print(f"[INFO] No {category} found.")

    if verbose:
        print("[INFO] Scan completed successfully.")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="To Detect sensitive Data in text file")
    parser.add_argument("file_path", help="path to the text file to scan")
    parser.add_argument("--verbose","-v", action="store_true",help="enable detailed output")

    args = parser.parse_args()

    ptf(args.file_path, args.verbose)
    

