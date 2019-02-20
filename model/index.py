from .db import DbConnect
from bs4 import BeautifulSoup
import requests
import re

class IndexModel(DbConnect):
    def __init__(self):
        super().__init__()
    
    def getList(self):
        self.connect()
        self.cursor.execute('select * from list order by id limit 5')
        result = self.cursor.fetchall()
        self.closeConnect()
        return result

    def getNotice(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        tags = soup.find_all('a', href=re.compile('.'))
        list = []
        for tag in tags:
            text = tag.get_text()
            href = tag['href']
            if re.search('研究生|硕士|调剂', text):
                link = {
                    'text': text,
                    'href': href
                }
                list.append(link)
        return list