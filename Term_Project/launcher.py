# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("Add new book: a")
    print("sEarch Book Title: e")
    print("Make html: m")
    print("----------------------------------------")
    print("Get crime data from year: g")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")

def PrintAYearMenu(year):
    print("========", year, "�⵵==========")
    print("������ ������ ����:  s")
    print("���˹߻� ��:  m")
    print("���˹߻��ð�:  t")
    print("���˹߻�����:  a")
    print("������ ���� ����:  mot")
    print("���˿� �������� ����:  r")
    print("������ ����� ���Ż���: men")
    print("���˵��� �� �Լ����: tool")
    print("������ �˰Ŵܼ�: c")
    print("========Menu==========")

def getCrimeDataFromYear(year):
    cselect = str(input('��� ����(����-1, ������-2) :'))
    PrintAYearMenu(year)
    select = str(input('�޴� ���� :'))

    if select == 'r':
        getRELATIONData(year, cselect)
    elif select == 'men':
        getMENTALData(year, cselect)
    elif select == 'tool':
        getTOOLData(year)
    elif select == 'c':
        getCLUEData(year, cselect)

def launcherFunction(menu):
    if menu == 'g':
        year = str(input('input year to get :'))
        getCrimeDataFromYear(year)
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    elif menu == 'q':
        QuitBookMgr()
    else:
        print ("error : unknow menu key")

def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")