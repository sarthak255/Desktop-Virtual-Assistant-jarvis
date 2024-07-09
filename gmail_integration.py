# src/gmail_integration.py
import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email
def send_email(subject, body, to_address):
    from_address = "your_email@gmail.com"
    password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

# Function to read emails
def read_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("your_email@gmail.com", "your_password")
    mail.select('inbox')
    
    status, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    
    for i in id_list:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                print(f"From: {email_from}\nSubject: {email_subject}\n")

# Test the Gmail functions
if __name__ == "__main__":
    send_email("Test Subject", "Test Body", "recipient_email@gmail.com")
    read_emails()
