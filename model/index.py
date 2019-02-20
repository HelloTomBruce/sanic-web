from .db import DbConnect

class IndexModel(DbConnect):
    def __init__(self):
        super().__init__()
    
    def getList(self):
        self.connect()
        self.cursor.execute('select * from list order by id limit 5')
        result = self.cursor.fetchall()
        self.closeConnect()
        return result
