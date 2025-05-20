import smtplib
from email.mime.text import MIMEText
from config import SMTP_USER, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT

def send_verification_email(email: str, token: str):
    link = f"http://localhost:3000/verify-email?token={token}"
    subject = "Verify your email"
    body = f"Click the link to verify your email: {link}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = email

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, email, msg.as_string())
    except Exception as e:
        print("Email sending failed:", e)
