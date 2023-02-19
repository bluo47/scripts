import smtplib
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


with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp_conn:
    smtp_conn.starttls() # Start a secure TLS connection
    smtp_conn.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Compose the email message
    sender = SMTP_USERNAME
    recipient = 'youremail@email.com'
    subject = 'Test email'
    body = 'This is a test email from Python'
    message = f'Subject: {subject}\n\n{body}'

    # Send the email
    smtp_conn.sendmail(sender, recipient, message)

print('Email sent successfully')
