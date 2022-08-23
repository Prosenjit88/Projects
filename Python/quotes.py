import smtplib, ssl
import datetime as dt
import random
from email.mime.text import MIMEText

day = dt.datetime.today().weekday()

def get_quote():
    with open('D:/Code/Projects/Projects/Python/quotes.txt') as f:
        lines = f.readlines()
        return random.choice(lines)

def send_email(quote):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "prosenjit15111988"  # Enter your address
    receiver_email = "prosenjit15111988@gmail.com"  # Enter receiver address
    password = "ejuihbylcybzoyim"
    message = MIMEText(quote)
    message['Subject'] = 'Inspiration'
    message['From'] = 'prosenjit15111988'
    message['To'] = 'prosenjit15111988@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


quote = get_quote()
send_email(quote)
