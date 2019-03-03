from .db import DbConnect
from bs4 import BeautifulSoup
import requests
import re
import time
from wxpy import *

class IndexModel(DbConnect):
    def __init__(self):
        super().__init__()
        self.funDict = {
            'yzw': self.getNoticeYZW,
            'xbsf': self.getNoticeXBSF,
            'jssf': self.getNoticeJSSF,
            'ynsf': self.getNoticeYNSF,
            'hnsf': self.getNoticeHNSF,
            'gxsf': self.getNoticeGXSF,
            'gzsf': self.getNoticeGZSF,
            'hainsf': self.getNoticdHAINSF,
            'ahsf': self.getNoticdAHSF,
            'ccsf': self.getNoticdCCSF,
            'hzsf': self.getNoticdHZSF,
            'scsf': self.getNoticdSCSF,
            'lnsf': self.getNoticdLNSF,
            'cqsf': self.getNoticdCQSF,
            'sysf': self.getNoticdSYSF,
            'mnsf': self.getNoticdMNSF,
            'gnsf': self.getNoticdGNSF,
            'tjsf': self.getNoticeTJSF,
            'hbsf': self.getNoticeHBSF
        }
        #self.bot = Bot()
        #self.friend = self.bot.friends().search('拾玖')[0]
    
    def getList(self):
        self.connect()
        self.cursor.execute('select * from list order by id limit 5')
        result = self.cursor.fetchall()
        self.closeConnect()
        return result
    
    def saveNotice(self, content):
        self.connect()
        self.cursor.execute('select * from notice where content="' + content + '";')
        result = self.cursor.fetchall()
        if len(result) == 0:
            self.cursor.execute('insert into notice (id, content) values (null, "' + content + '");')
            self.connection.commit()
            self.closeConnect()
            return True
        else:
            self.closeConnect()
            return False

    def getNotice(self, url, encodeType, urlType):
        return self.funDict[urlType](url, encodeType)

    
    def getNoticeYZW(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        ul = soup.find('ul', {"class": "news-list"})
        liList = ul.find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a', href=re.compile('.'))
            text = aTag.get_text()
            href = aTag['href']
            timeTag = li.find('span', {'class': "span-time"})
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticeXBSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find_all('li', {'class': 'a-list'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a', href=re.compile('.'))
            text = aTag.get_text()
            href = aTag['href']
            timeTag = li.find('span', {'class': "pdate"})
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res

    def getNoticeJSSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        tableTag = soup.find('table', {'class': 'wp_article_list_table'})
        tdList = tableTag.find_all('td')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for td in tdList:
            aTag = td.find('a', href=re.compile('.'))
            text = aTag.get_text()
            href = aTag['href']
            timeTag = td.find('span', {'class': "bg-success"})
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticeYNSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        ul = soup.find('ul', {'class': 'e2'})
        liList = ul.find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a', {'class': 'title', 'href': re.compile('.')})
            text = aTag.get_text()
            href = aTag['href']
            timeParentTag = li.find('span', {'class': "info"})
            timeTag = timeParentTag.find('span')
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y/%m/%d %H:%M:%S')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res

    def getNoticeHNSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        tdList = soup.find_all('td', {'height': '28'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for td in tdList:
            aTag = td.find('a', {'href': re.compile('.')})
            text = aTag.get_text()
            href = aTag['href']
            timeTag = td.find_next_sibling()
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticeGXSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        tableTag = soup.find('table', {'class': 'k2list'})
        trList = tableTag.find_all('tr')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for tr in trList:
            td = tr.find('td', {'class': 'dotline'})
            aTag = td.find('a', {'href': re.compile('.')})
            text = aTag.get_text()
            href = aTag['href']
            timeTag = td.find_next_sibling()
            publishTime = timeTag.get_text()
            timeTu = time.strptime(publishTime, '%Y/%m/%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticeGZSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        aList = soup.find_all('a', {'class': 'c41515'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for aTag in aList:
            text = aTag.get_text()
            href = aTag['href']
            timeTag = aTag.find_parent().find_next_sibling()
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdHAINSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        aList = soup.find_all('a', {'class': 'news-link'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for aTag in aList:
            text = aTag.get_text()
            href = aTag['href']
            timeTag = aTag.find_parent().find_next_sibling()
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y/%m/%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdAHSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        aList = soup.find_all('a', {'class': 'itemtitle'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for aTag in aList:
            text = aTag.get_text()
            href = aTag['href']
            timeTag = aTag.find_parent().find_next_sibling()
            publishTime = timeTag.get_text().strip()[1:-1]
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdCCSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        trList = soup.find_all('tr', {'height': '20'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for tr in trList:
            aTagParent = tr.find('td', {'width': '100%'})
            aTag = aTagParent.find('a')
            text = aTag.get_text()
            href = aTag['href']
            timeTag = aTag.find_parent().find_next_sibling().find('span')
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y/%m/%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res

    def getNoticdHZSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        ul = soup.find('ul', {'class': 'container-right-ul'})
        liList = ul.find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.find('div', {'class', 'gg-title'}).get_text()
            href = aTag['href']
            timeTag = aTag.find('div', {'class': 'gg-date'})
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdSCSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        tableList = soup.find('div', {'class': 'div_items'}).find_all('table', {'class': 'table_item'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for table in tableList:
            aTag = table.find('td', {'align': 'left'}).find('a')
            text = aTag.get_text()
            href = aTag['href']
            timeTag = table.find('td', {'align': 'right'}).find('div')
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdLNSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find('div', {'class': 'list'}).find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.get_text()
            href = aTag['href']
            timeTag = li.find('span')
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdCQSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find('div', {'class': 'bd hei938'}).find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            if aTag == None:
                continue
            text = aTag.get_text()
            href = aTag['href']
            timeTag = li.find('span')
            publishTime = timeTag.get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdSYSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find_all('span', {'class': 'Article_Title'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.get_text()
            href = aTag['href']
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': ''
                }
                resultList.append(link)
                if re.search('调剂', text):
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdMNSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find_all('td', {'class': 'heise1301'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.get_text()
            href = aTag['href']
            publishTime = li.get_text().strip()[-11:-1]
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticdGNSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find_all('td', {'width': '560px'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.get_text()
            href = aTag['href']
            publishTime = li.find_next_sibling().get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def getNoticeTJSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find_all('tr', {'height': '20'})
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('a')
            text = aTag.get_text()
            href = aTag['href']
            publishTime = li.find('span', {'class': 'timestyle49030'}).get_text().strip()
            timeTu = time.strptime(publishTime, '%Y/%m/%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res

    def getNoticeHBSF(self, url, encodeType):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html5lib', from_encoding = encodeType)
        liList = soup.find('div', {'class': 'articles'}).find_all('li')
        resultList = []
        res = {
            'notice': 0,
            'list': []
        }
        for li in liList:
            aTag = li.find('span', {'class': 'title'}).find('a')
            text = aTag.get_text()
            href = aTag['href']
            publishTime = li.find('span', {'class': 'date'}).get_text().strip()
            timeTu = time.strptime(publishTime, '%Y-%m-%d')
            years = int(timeTu[0])
            if re.search('研究生|硕士|调剂', text) and len(text) > 5:
                link = {
                    'text': text,
                    'href': href,
                    'time': publishTime
                }
                resultList.append(link)
                if re.search('调剂', text) and years == 2019:
                    res['notice'] = 1
                    result = self.saveNotice(text + url)
                    if result:
                        self.sendMsg(text, url)
        res['list'] = resultList
        return res
    
    def sendMsg(self, msg, url):
        return
        #self.friend.send(msg + '\n' + url)