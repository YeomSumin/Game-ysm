# -*- coding: cp949 -*-
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
CrimeDoc = None
CSelect = None
# regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'PGM0C0ZXEQ3U3XV0CURV'

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

def PrintAYearMenu(year):
    print("========", year, "년도==========")
    print("피해자 성별과 연령:  s")
    print("범죄발생 월:  m")
    print("범죄발생시간:  t")
    print("범죄발생지역:  a")
    print("범죄자 범행 동기:  mot")
    print("범죄자 정신 상태:  men")
    print("범죄자와 피해자와의 관계:  r")
    print("범죄도구 및 입수방법:  too")
    print("범죄자 검거단서:  c")
    print("========Menu==========")

def getCrimeDataFromYear(year):
    global CSelect
    cselect = str(input('사건 선택(살인-1, 성폭행-2) :'))
    PrintAYearMenu(year)
    CSelect = cselect
    select = str(input('메뉴 선택 :'))

    if select == 's':
        getSexData(year, cselect)
    elif select == 'm':
        getMonthData(year, cselect)
    elif select == 't':
        getTimeData(year, cselect)
    elif select == 'a':
        getAreaData(year, cselect)
    elif select == 'mot':
        getMotivData(year, cselect)
    elif select == 'men':
        getMENTALData(year, cselect)
    elif select == 'r':
        getRELATIONData(year, cselect)
    elif select == 'too':
        getTOOLData(year, cselect)
    elif select == 'c':
        getCLUEData(year, cselect)


def getSexData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 25):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="15", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 25):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="227", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getMonthData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        print("해당 년도의 데이터가 없습니다.")
    else:
        if crime == "1":    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 17):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="180", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getTimeData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 13):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="6", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 14):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="182", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getAreaData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        print("해당 년도의 데이터가 없습니다.")
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 22):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="185", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getMotivData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 22):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="57", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 26):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="224", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getMENTALData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
       if (crime == "1"): itemcode = "7"
       else: itemcode = "10"
       for i in range(7, 25):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="56", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if (crime == "1"): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(7, 25):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                STAT_CODE="208", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)

def getRELATIONData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if (crime == '1'): itemcode = "7"
        else: itemcode = "10"
        for i in range(5, 19):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="53", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if (crime == '1'): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(5, 19):
          uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                               STAT_CODE="229", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
          conn.request("GET", uri)
          getData(year)

def getTOOLData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        for r in range(420, 427):
            for i in range(5, 19):
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                     STAT_CODE="36", ITEM_CODE1=str(r), ITEM_CODE2=str(i))
                conn.request("GET", uri)
                getData(year)
    else:
        for r in range(420, 427):
            for i in range(5, 19):
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                     STAT_CODE="190", ITEM_CODE1=str(r), ITEM_CODE2=str(i))
                conn.request("GET", uri)
                getData(year)

def getCLUEData(year, crime):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if(crime == "1"): itemcode = "7"
        else: itemcode = "10"
        for i in range(5, 27):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="40", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)
    else:
        if(crime == "1"): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(5, 27):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="172", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            conn.request("GET", uri)
            getData(year)


def getData(year):
    global CrimeDoc
    req = conn.getresponse()
    #print(req.status)
    if int(req.status) == 200:
        CrimeDoc = req.read().decode('utf-8')
        PrintSearchData()
        #return extractBookData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def PrintSearchData():
    global CrimeDoc, CSelect

    parseData = parseString(CrimeDoc)
    GeoInfoLibrary = parseData.childNodes
    row = GeoInfoLibrary[0].childNodes

    for item in row:
        # print(item.nodeName)
        if item.nodeName == "row":
            subitems = item.childNodes

            print("==========================================")
            if subitems[1].firstChild is not None:
                print("<", subitems[1].firstChild.nodeValue, "년도>  ", sep="", end="");
                if CSelect == '1' : print("<살인>")
                else: print("<성폭행>")
            if subitems[5].firstChild is not None:
                print(subitems[5].firstChild.nodeValue, " - ", sep="", end="");
            if subitems[13].firstChild is not None:
                print(subitems[13].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[15].firstChild is not None:
                print("계: ", subitems[15].firstChild.nodeValue, ", ", sep="", end="");
            print()
            print("==========================================")


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



"""
def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("row")  # return list type
    #print(itemElements)
    for item in itemElements:
        isbn = item.find("BASE_YEAR")
        strTitle = item.find("STAT_NAME")
        print(isbn)
        if len(strTitle.text) > 0:
            return {"ISBN": isbn.text, "title": strTitle.text}
"""