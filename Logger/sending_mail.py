import smtplib

# E-Mail-Konfiguration
sender_email = 'testlf8code@gmail.com'
receiver_email = 'testlf8code@gmail.com'
password = 'muhuetrlghvexkrz'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Funktion zum Senden der E-Mail
def send_email(subject, body):
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        message = 'Subject: {}\n\n{}'.format(subject, body)
        server.sendmail(sender_email, receiver_email, message)

