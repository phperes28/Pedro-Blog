import smtplib
import os


class Email:

    def send_email(self, name, email, phone, message):
        server = smtplib.SMTP('smtp.gmail.com')
        server.ehlo()

        server.starttls()  #secures connection
        server.login(user= os.environ.get("MY_EMAIL"), password=os.environ.get("PASS"))
        server.sendmail(
            from_addr= os.environ.get("MY_EMAIL"),
            to_addrs= os.environ.get("MY_EMAIL"),
            msg= f'Subject: New contact from{name} \n\n{name}\n{email}\n{phone}\n{message}.'
            )
