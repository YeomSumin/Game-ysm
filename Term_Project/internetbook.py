# -*- coding: cp949 -*-
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
# regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'BZ9VPQBK6Y4W7CS84PP0'

# 네이버 OpenAPI 접속 정보 information
server = "openapi.crimestats.or.kr:8080"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, **user):
    # str = "http://" + server + "/search" + "?"
    str = "https://" + server + "/WiseOpen/ArcData" + "/" + regKey + "/xml"
    for key in user.keys():
        str += "/" + user[key]  # 어떻게 고치지
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getCrimeDataFromYEAR(isbn):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=isbn, STAT_CODE="1", ITEM_CODE1="7", ITEM_CODE2="5")
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        print(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getCrimeDataFromAGE():
    for j in range(2010, 2014):
        base_year = str(j)
        for i in range(5, 25):
            item_code2 = str(i)
            global server, regKey, conn
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="15", ITEM_CODE1="7", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

    for j in range(2014, 2016):
        base_year = str(j)
        for i in range(5, 27):
            item_code2 = str(i)
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="227", ITEM_CODE1="10211", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

def getCrimeDataFromRELATION():
    for j in range(2010, 2014):
        base_year = str(j)
        for i in range(5, 19):
            item_code2 = str(i)
            global server, regKey, conn
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="53", ITEM_CODE1="7", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

    for j in range(2014, 2016):
        base_year = str(j)
        for i in range(5, 19):
            item_code2 = str(i)
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="229", ITEM_CODE1="10211", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

def getCrimeDataFromMENTAL():
    for j in range(2010, 2014):
        base_year = str(j)
        for i in range(7, 25):
            item_code2 = str(i)
            global server, regKey, conn
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="56", ITEM_CODE1="7", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

    for j in range(2014, 2016):
        base_year = str(j)
        for i in range(7, 25):
            item_code2 = str(i)
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="208", ITEM_CODE1="10211", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

def getCrimeDataFromTOOL():
    for j in range(2010, 2014):
        base_year = str(j)
        for r in range(420, 427):
            item_code1 = str(r)
            for i in range(5, 19):
                item_code2 = str(i)
                global server, regKey, conn
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="36", ITEM_CODE1=item_code1, ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None

    for j in range(2014, 2016):
        base_year = str(j)
        for r in range(420, 427):
            item_code1 = str(r)
            for i in range(5, 19):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="190",
                                     ITEM_CODE1=item_code1, ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None

def getCrimeDataFromCLUE():
    for j in range(2010, 2014):
        base_year = str(j)
        for i in range(5, 27):
            item_code2 = str(i)
            global server, regKey, conn
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="40", ITEM_CODE1="7", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

    for j in range(2014, 2016):
        base_year = str(j)
        for i in range(5, 27):
            item_code2 = str(i)
            if conn == None:
                connectOpenAPIServer()
            # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="172", ITEM_CODE1="10211", ITEM_CODE2=item_code2)
            conn.request("GET", uri)

            req = conn.getresponse()
            print(req.status)
            if int(req.status) == 200:
                print("Book data downloading complete!")
                print(req.read().decode('utf-8'))
            else:
                print("OpenAPI request has been failed!! please retry")
                return None

"""
def extractBookData(strXml):
    #from xml.etree import ElementTree
    #tree = ElementTree.fromstring(strXml)
    print(strXml)

    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("row")  # return list type
    print(itemElements)
    for item in itemElements:
        isbn = item.find("BASE_YEAR")
        strTitle = item.find("STAT_NAME")
        print(strTitle)
        if len(strTitle.text) > 0:
            return {"ISBN": isbn.text, "title": strTitle.text}
"""

def sendMain():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    msgtext = str(input('write message :'))
    passwd = str(input(' input your password of gmail account :'))
    msgtext = str(input('Do you want to include book data (y/n):'))
    if msgtext == 'y':
        keyword = str(input('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('EUC-KR'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server 종료합니다.


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True