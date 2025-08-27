import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Get today's date and define the filename
today = datetime.today().strftime("%Y-%m-%d")
file_name = f"sales_report_{today}.xlsx"
file_path = os.path.join("output", file_name)

# 2. Email configuration from .env
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
app_password = os.getenv("EMAIL_PASSWORD")

subject = f"Daily Sales Report – {today}"
body = (
    "Hi,\n\n"
    "Please find attached the daily sales report.\n\n"
    "Best regards,\n"
    "Automated Reporting System"
)

# 3. Create email message
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# 4. Attach the Excel report
with open(file_path, "rb") as f:
    file_data = f.read()
    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=file_name
    )

# 5. Send email via SMTP (Gmail example)
smtp_server = "smtp.gmail.com"
smtp_port = 587

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    print("✅ Email sent successfully!")
