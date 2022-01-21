import sqlite3
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from DataBaseConnection import DataBaseConnection
from string import Template

sql_insert = """INSERT INTO user (username, email, pwd) VALUES(%s, %s, %s)"""
sql_select = """SELECT * FROM user WHERE email = %s"""

database = DataBaseConnection()

MY_ADDRESS = ' '
PASSWORD = ' '


class UserService(object):

    def __init__(self):
        self.connection = database.conn

    def addUser(self, User):
        try:
            user = (User.username, User.email, User.password)
            cursor = self.connection.cursor()
            cursor.execute(sql_insert, user)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Failed to add to table", error)

    def findUser(self, email):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_select, (email,))
            user = cursor.fetchone()
            return user
        except sqlite3.Error as error:
            print("Failed to add to table", error)

    def read_template(self,filename):
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)
    
    def send_mail(self, email, username):
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        message_template = self.read_template('message.txt')
        msg = MIMEMultipart()  # create a message
        code = random.randint(1000, 9999)
        # add parameters the message template
        message = message_template.substitute(PERSON_NAME=username, CODE=code)

        # the message parameters 
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Email Validation"

        #  message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message 
        s.send_message(msg)
        return code
