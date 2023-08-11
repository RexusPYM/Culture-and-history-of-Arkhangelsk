import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(text: str, addr_to: list[str]):
    sender_data = {
        'login': '',
        'password': '',
        'smtp_server': '',
        'smtp_server_port': '',
    }

    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msg['From'] = sender_data['login']
    msg['Subject'] = 'Новый исторический объект'
    msg['To'] = ', '.join(addr_to)

    try:
        server = smtplib.SMTP(sender_data['smtp_server'], int(sender_data['smtp_server_port']))
        server.starttls()
        server.login(sender_data['login'], sender_data['password'])
        server.send_message(msg)
        print('mails were sended')
        server.quit()
    except Exception as ex:
        print(ex)
