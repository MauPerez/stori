import email
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


class Email:
    def __init__(self, total_balance, avg_credit, avg_debit, months) -> None:
        self.sender = os.getenv("SENDER")
        self.receiver = os.getenv("RECEIVER")
        self.total_balance = total_balance
        self.avg_credit = avg_credit
        self.avg_debit = avg_debit
        self.months = months

    def create_email_file(self, file_name, file_handler):
        data = {
            "Total balance": self.total_balance,
            "Months": self.months,
            "Average debit amount": self.avg_debit,
            "Average credit amount": self.avg_credit,
        }
        file_handler.create(file_name, data=data)

    def send_email(self, file_path):
        msg = MIMEMultipart()
        body_part = MIMEText("Please find attach your transactions", "plain")
        msg.attach(body_part)

        with open(file_path, "rb") as file:
            msg.attach(MIMEApplication(file.read(), Name=f"{file_path}"))

        msg["Subject"] = f"The contents of {file_path}"
        msg["From"] = self.sender
        msg["To"] = self.receiver

        s = smtplib.SMTP("smtp.live.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(os.getenv("USER"), os.getenv("PASS"))
        s.sendmail(self.sender, [self.receiver], msg.as_string())
        print("Sent")
        s.quit()
