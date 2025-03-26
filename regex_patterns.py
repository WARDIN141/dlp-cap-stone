import re

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


sample_text = """
Dear Support Team,  

I have a few details to update in your system. My personal email is john.doe123@gmail.com, and my work email is john.doe@corporate-tech.co.uk.  
You can reach me at +91-9876543210 or my secondary number 9123456789.  

For payment, I usually use my Visa card: 4111-1111-1111-1111 or my Amex: 3712 345678 90123.  
My Mastercard is 5555 6666 7777 8888, but I rarely use it.  

As for passwords, I used to have weak ones like "password123" and "Hello123!", but now I use stronger ones like "StrongPass@2024" and "UltraSafe#99".  
I want to ensure that bad passwords like "admin123", "qwerty@123", and "P@ssword1234" are not detected as secure.  

Looking forward to your response.  

Best regards,  
John Doe  

"""




print("Emails:", ee(sample_text))
print("Phone Numbers:", epn(sample_text))
print("Credit Card Numbers:", eccn(sample_text))
print("Possible Passwords:", ep(sample_text))
