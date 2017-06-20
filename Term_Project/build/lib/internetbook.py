#-*- coding: utf-8 -*-
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from tkinter import *
from tkinter import font
import tkinter.messagebox


##global
conn = None
CrimeDoc = None
CSelect = None
uri = None
URI = None

g_Tk = Tk()
g_Tk.geometry("1000x600+750+200")
DataList = []
uri = URI
# regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'PGM0C0ZXEQ3U3XV0CURV'

print("\n")
# 네이버 OpenAPI 접속 정보 information
server = "openapi.crimestats.or.kr:8080"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def returnURI():
    return URI

def userURIBuilder(server, **user):
    # str = "http://" + server + "/search" + "?"
    str = "https://" + server + "/WiseOpen/ArcData" + "/" + regKey + "/xml"
    #for key in user.keys():
    #    str += "/" + user[key]  # 어떻게 고치지
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


def getSexData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 25):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="15", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/15/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 25):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="227", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/227/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getMonthData(year, crime):
    global server, regKey, conn, uri, URI
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
            URI = uri + "/1" + "/10/" + year + "/180/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getTimeData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 13):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="6", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/6/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 14):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="182", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/182/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getAreaData(year, crime):
    global server, regKey, conn, uri, URI
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
            URI = uri + "/1" + "/10/" + year + "/185/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getMotivData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if crime == '1':    itemcode = "7"
        else:   itemcode = "10"
        for i in range(5, 22):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="57", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/57/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if crime == '1':    itemcode = "10208"
        else:   itemcode = "10211"
        for i in range(5, 26):
            uri = userURIBuilder(server, start="1", end="10", BASE_YEAR=year, STAT_CODE="224", ITEM_CODE1=itemcode,
                                 ITEM_CODE2=str(i))
            URI = uri + "/1" + "/10/" + year + "/224/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getMENTALData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
       if (crime == "1"): itemcode = "7"
       else: itemcode = "10"
       for i in range(7, 25):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="56", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            URI = uri + "/1" + "/500/" + year + "/500/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if (crime == "1"): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(7, 25):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                STAT_CODE="208", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            URI = uri + "/1" + "/500/" + year + "/208/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)

def getRELATIONData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if (crime == '1'): itemcode = "7"
        else: itemcode = "10"
        for i in range(5, 19):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="53", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            URI = uri + "/1" + "/500/" + year + "/53/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if (crime == '1'): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(5, 19):
          uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                               STAT_CODE="229", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
          URI = uri + "/1" + "/500/" + year + "/229/" + itemcode +"/" + str(i)
          conn.request("GET", uri)
          getData(year)

def getTOOLData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        for r in range(420, 427):
            for i in range(5, 19):
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                     STAT_CODE="36", ITEM_CODE1=str(r), ITEM_CODE2=str(i))
                URI = uri + "/1" + "/500/" + year + "/36/" + str(r) +"/" + str(i)
                conn.request("GET", uri)
                getData(year)
    else:
        for r in range(420, 427):
            for i in range(5, 19):
                uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                     STAT_CODE="190", ITEM_CODE1=str(r), ITEM_CODE2=str(i))
                URI = uri + "/1" + "/500/" + year + "/190/" + str(r) +"/" + str(i)
                conn.request("GET", uri)
                getData(year)

def getCLUEData(year, crime):
    global server, regKey, conn, uri, URI
    if conn == None:
        connectOpenAPIServer()

    if year != "2014" and year != "2015":
        if(crime == "1"): itemcode = "7"
        else: itemcode = "10"
        for i in range(5, 27):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="40", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            URI = uri + "/1" + "/500/" + year + "/40/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)
    else:
        if(crime == "1"): itemcode = "10208"
        else: itemcode = "10211"
        for i in range(5, 27):
            uri = userURIBuilder(server, start="1", end="500", BASE_YEAR=year,
                                 STAT_CODE="172", ITEM_CODE1=itemcode, ITEM_CODE2=str(i))
            URI = uri + "/1" + "/500/" + year + "/172/" + itemcode +"/" + str(i)
            conn.request("GET", uri)
            getData(year)


def getData(year):
    global CrimeDoc
    req = conn.getresponse()
    #print(req.status)
    if int(req.status) == 200:
        CrimeDoc = req.read().decode('utf-8')
        SearchLibrary()
        #PrintSearchData()
        #return extractBookData(req.read().decode('utf-8'))
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[범죄 분석 App]")
    MainText.pack()
    MainText.place(x=20)


def InitSearchListBox():
    # 데이터조회
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=445, y=175)
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=30, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(0, "피해자 성별과 연령(1964~2015)")
    SearchListBox.insert(1, "범죄발생 월(2014~2015)")
    SearchListBox.insert(2, "범죄발생시간(1964~2015)")
    SearchListBox.insert(3, "범죄발생지역(2014~2015)")
    SearchListBox.insert(4, "범죄자 범행 동기(1972~2015)")
    SearchListBox.insert(5, "범죄자 정신상태(1972~2015")
    SearchListBox.insert(6, "범죄자와 피해자와의 관계")
    SearchListBox.insert(7, "범죄도구 및 입수방법")
    SearchListBox.insert(8, "범죄자 검거단서")
    SearchListBox.pack()
    SearchListBox.place(x=90, y=175)
    ListBoxScrollbar.config(command=SearchListBox.yview)

    # 차트조회
    global SearchListBox2
    ListBoxScrollbar2 = Scrollbar(g_Tk)
    ListBoxScrollbar2.pack()
    ListBoxScrollbar2.place(x=445, y=450)
    #TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox2 = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=30, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar2.set)

    SearchListBox2.insert(0, "범죄발생 월(2014~2015)")
    SearchListBox2.insert(1, "범죄발생시간(2014~2015)")
    SearchListBox2.insert(2, "범죄발생지역(2014~2015)")
    SearchListBox2.pack()
    SearchListBox2.place(x=90, y=450)
    ListBoxScrollbar2.config(command=SearchListBox2.yview)


def InitInputLabel():
    global InputLabel, InputLabel2, InputLabel3, InputLabel4, v1, v2, v3, v4
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')

    # 데이터 조회
    # 년도
    v1 = StringVar()
    InputLabel = Entry(g_Tk, font = TempFont, width = 30, borderwidth = 12, relief = 'ridge', textvariable=v1)
    InputLabel.pack()
    InputLabel.place(x=90, y=75)
    #사건
    v2 = StringVar()
    InputLabel2 = Entry(g_Tk, font=TempFont, width=30, borderwidth=12, relief='ridge', textvariable=v2)
    InputLabel2.pack()
    InputLabel2.place(x=90, y=125)

    # 차트 조회
    # 년도
    v3 = StringVar()
    InputLabel3 = Entry(g_Tk, font=TempFont, width=30, borderwidth=12, relief='ridge', textvariable=v3)
    InputLabel3.pack()
    InputLabel3.place(x=90, y=350)
    # 사건
    v4 = StringVar()
    InputLabel4 = Entry(g_Tk, font=TempFont, width=30, borderwidth=12, relief='ridge', textvariable=v4)
    InputLabel4.pack()
    InputLabel4.place(x=90, y=400)

    l1 = Label(g_Tk, text="년도")
    l2 = Label(g_Tk, text="사건")
    l3 = Label(g_Tk, text="세부사항")
    l4 = Label(g_Tk, text="< 데이터 조회 >")
    l5 = Label(g_Tk, text="< 차트 조회 >")
    l6 = Label(g_Tk, text="년도")
    l7 = Label(g_Tk, text="사건")
    l8 = Label(g_Tk, text="세부사항")
    l1.pack(); l2.pack(); l3.pack(); l4.pack();
    l5.pack(); l6.pack(); l7.pack(); l8.pack();
    l1.place(x=35, y=90); l2.place(x=35, y=140); l3.place(x=25, y=190); l4.place(x=10, y=50);
    l5.place(x=10, y=320); l6.place(x=35, y=370); l7.place(x=35, y=420); l8.place(x=25, y=470);


def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')

    #데이터 조회
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=240, y=235)

    # 차트 조회
    SearchButton2 = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction2)
    SearchButton2.pack()
    SearchButton2.place(x=240, y=505)

def SearchButtonAction():
    global SearchListBox, CSelect
    global InputLabel, InputLabel2, v1, v2
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    #ret = getCrimeDataFromYear(InputLabel)
    #AddBook(ret)

    if (v2.get() == "살인"):
        CSelect = '1';
    else:
        CSelect = '2';

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    # 데이터 조회
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        getSexData(v1.get(), CSelect)
    elif iSearchIndex == 1:
        getMonthData(v1.get(), CSelect)
    elif iSearchIndex == 2:
        getTimeData(v1.get(), CSelect)
    elif iSearchIndex == 3:
        getAreaData(v1.get(), CSelect)
    elif iSearchIndex == 4:
        getMotivData(v1.get(), CSelect)
    elif iSearchIndex == 5:
        getMENTALData(v1.get(), CSelect)
    elif iSearchIndex == 6:
        getRELATIONData(v1.get(), CSelect)
    elif iSearchIndex == 7:
        getTOOLData(v1.get(), CSelect)
    elif iSearchIndex == 8:
        getCLUEData(v1.get(), CSelect)

    SearchLibrary()

    RenderText.configure(state='disabled')

def SearchButtonAction2():
    global SearchListBox2
    global InputLabel3, InputLabel4, v3, v4

    # 차트 조회
    iSearchIndex2 = SearchListBox2.curselection()[0]
    if iSearchIndex2 == 0:
        if (v4.get() == "살인"):
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_murder_month.gif')
            else:
                img = PhotoImage(file='2015_murder_month.gif')
        else:
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_violence_month.gif')
            else:
                img = PhotoImage(file='2015_violence_month.gif')
    elif iSearchIndex2 == 1:
        if (v4.get() == "살인"):
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_murder_time.gif')
            else:
                img = PhotoImage(file='2015_murder_time.gif')
        else:
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_violence_time.gif')
            else:
                img = PhotoImage(file='2015_violence_time.gif')
    elif iSearchIndex2 == 2:
        if (v4.get() == "살인"):
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_murder_region.gif')
            else:
                img = PhotoImage(file='2015_murder_region.gif')
        else:
            if (v3.get() == "2014"):
                img = PhotoImage(file='2014_violence_region.gif')
            else:
                img = PhotoImage(file='2015_violence_region.gif')

    lbl = Label(image=img)
    lbl.image = img
    lbl.pack(side=RIGHT)
    lbl.place(x=490, y=150)

def SearchLibrary():
    global CSelect, DataList
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.crimestats.or.kr:8080")
    conn.request("GET", returnURI())
    req = conn.getresponse()
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[1].firstChild is not None:
                        RenderText.insert(INSERT, "<")
                        RenderText.insert(INSERT, subitems[1].firstChild.nodeValue)
                        RenderText.insert(INSERT, "년도>  ")
                        if CSelect == '1':
                            RenderText.insert(INSERT, "<살인>")
                        else:
                            RenderText.insert(INSERT, "<성폭행>")
                    RenderText.insert(INSERT, "\n"),
                    if subitems[5].firstChild is not None:
                        RenderText.insert(INSERT, subitems[5].firstChild.nodeValue)
                        RenderText.insert(INSERT, " - ")
                    if subitems[13].firstChild is not None:
                        RenderText.insert(INSERT, subitems[13].firstChild.nodeValue)
                        RenderText.insert(INSERT, ", ")
                    if subitems[15].firstChild is not None:
                        RenderText.insert(INSERT, "계: ")
                        RenderText.insert(INSERT, subitems[15].firstChild.nodeValue)
                        RenderText.insert(INSERT, ", ")
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "==========================================")
                    RenderText.insert(INSERT, "\n\n\n\n\n")


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=540, y=115)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')




InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()
