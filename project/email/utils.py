import smtplib
from typing import Dict
from environs import Env
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    @staticmethod
    def send_message(email: Dict[str,str], message: str):
        env = Env()
        env.read_env()

        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(env('EMAIL_ADDRESS'), env('EMAIL_PASSWORD'))

        msg = MIMEMultipart()

        msg['From']=env('EMAIL_ADDRESS')
        msg['To']=email['recipient']
        msg['Subject']=email['subject']
        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)
        del msg

        server.quit()
