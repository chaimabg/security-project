import mysql.connector

class DataBaseConnection(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="projetsecurite")

