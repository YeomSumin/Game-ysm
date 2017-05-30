# -*- coding: cp949 -*-
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
global CrimeDoc
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
    global CrimeDoc
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=isbn, STAT_CODE="1", ITEM_CODE1="7", ITEM_CODE2="5")
    conn.request("GET", uri)

    req = conn.getresponse()
    #print(req.status)
    if int(req.status) == 200:
        CrimeDoc = req.read().decode('utf-8')
        PrintSearchData()
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getData(year):
    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        print(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getAGEData(year, crime):
    base_year = str(year)
    if base_year != "2014" and base_year != "2015":
        if (crime == "1"):
            for i in range(5, 25):
                item_code2 = str(i)
                global server, regKey, conn
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="15", ITEM_CODE1="7",
                                     ITEM_CODE2=item_code2)
                conn.request("GET", uri)
                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
        else:
            for i in range(5, 25):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="15", ITEM_CODE1="10",
                                     ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None

    else:
        if (crime == "1"):
            for i in range(5, 27):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="227", ITEM_CODE1="10208", ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
        else:
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

def getRELATIONData(year, crime):
    base_year = str(year)
    if base_year != "2014" and base_year != "2015":
        if (crime == '1'):
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
        else:
            for i in range(5, 19):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="53", ITEM_CODE1="10", ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
    else:
        if(crime == "1"):
            for i in range(5, 19):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="229", ITEM_CODE1="10208", ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
        else:
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

def getMENTALData(year, crime):
    base_year = str(year)
    if base_year != "2014" and base_year != "2015":
       if (crime == "1"):
            for i in range(7, 25):
                item_code2 = str(i)
                global server, regKey, conn
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="56", ITEM_CODE1="7", ITEM_CODE2=item_code2)
                conn.request("GET", uri)
       else:
            for i in range(7, 25):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="56", ITEM_CODE1="10", ITEM_CODE2=item_code2)
                conn.request("GET", uri)
                getData(year)

    else:
        if (crime == "1"):
            for i in range(7, 25):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="208", ITEM_CODE1="10208", ITEM_CODE2=item_code2)
                conn.request("GET", uri)
                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
        else:
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

def getTOOLData(year):
    base_year = str(year)
    if base_year != "2014" and base_year != "2015":
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
    else:
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

def getCLUEData(year, crime):
    base_year = str(year)
    if base_year != "2014" and base_year != "2015":
        if(crime == "1"):
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
        else:
            for i in range(5, 27):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="40", ITEM_CODE1="10", ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None

    else:
        if(crime == "1"):
            for i in range(5, 27):
                item_code2 = str(i)
                if conn == None:
                    connectOpenAPIServer()
                # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=base_year, STAT_CODE="172", ITEM_CODE1="10208", ITEM_CODE2=item_code2)
                conn.request("GET", uri)

                req = conn.getresponse()
                print(req.status)
                if int(req.status) == 200:
                    print("Book data downloading complete!")
                    print(req.read().decode('utf-8'))
                else:
                    print("OpenAPI request has been failed!! please retry")
                    return None
        else:
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

def PrintSearchData():
    global CrimeDoc

    parseData = parseString(CrimeDoc)
    GeoInfoLibrary = parseData.childNodes
    row = GeoInfoLibrary[0].childNodes

    for item in row:
        # print(item.nodeName)
        if item.nodeName == "row":
            subitems = item.childNodes

            if subitems[1].firstChild is not None:
                print(subitems[1].firstChild.nodeValue, "년도 - ", sep="", end="");
            if subitems[5].firstChild is not None:
                print(subitems[5].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[13].firstChild is not None:
                print("성별과 연령: ", subitems[13].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[15].firstChild is not None:
                print("계: ", subitems[15].firstChild.nodeValue, ", ", sep="", end="");
            print()

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

def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for bookitem in BookList:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("Title:" + bookitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()

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