import pymysql

class DbConnect():
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'zyw123',
            db = 'notice',
            charset = 'utf8'
        )
        self.cursor = self.connection.cursor()
    
    def closeCursor(self):
        self.cursor.close()
    
    def closeConnect(self):
        self.connection.close()