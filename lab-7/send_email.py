import smtplib
import os
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Retrieve from environment

msg = MIMEText("This is a secure email.")
msg["Subject"] = "Secure Email"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "recipient@example.com"

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, "recipient@example.com", msg.as_string())    server.quit()
    print("Email sent securely!")
except Exception as e:
    print("Error:", e)
