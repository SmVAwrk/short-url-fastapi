import smtplib
import ssl

from .config import EMAIL_PORT, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def send_email(
        receiver_email,
        message,
        port=EMAIL_PORT,
        smtp_server=EMAIL_HOST,
        sender_email=EMAIL_HOST_USER,
        password=EMAIL_HOST_PASSWORD
):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
