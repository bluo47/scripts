import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Set up the SMTP connection
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

print("** SMTP Parameters: ")
print(SMTP_SERVER)
print(SMTP_PORT)
print(SMTP_USERNAME)
i = 0

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp_conn:
    smtp_conn.starttls() # Start a secure TLS connection
    smtp_conn.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Compose the email message
    sender = SMTP_USERNAME
    recipient = 'youremail@email.com'
    subject = 'Test email with attachment'
    body = 'This is a test email with an attachment from Python'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # Add the attachment
    filename = 'WHO-COVID-19-global-data.csv.zip'
    with open(filename, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('content-disposition', 'attachment', filename=filename)
        i = i + 1
        msg.attach(attachment)

    # Send the email
    smtp_conn.send_message(msg)

print('Email sent successfully')
print('Attachment: ' + str(i))
