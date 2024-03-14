import smtplib

email = ""
email_password = ""


class NotificationManager:

    def send_email(self, message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=email_password)
        email_message = f"Subject: Flight deal!\n\n{message}"
        encoded_message = email_message.encode('utf-8')

        connection.sendmail(from_addr=email,
                            to_addrs="@gmail.com",
                            msg=encoded_message
                            )
        connection.close()
