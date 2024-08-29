import smtplib, ssl
from credentials import email_username, email_password  # Importing the credentials

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = email_username  # Use the imported username
    password = email_password  # Use the imported password

    receiver = "darioggalvagno@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
