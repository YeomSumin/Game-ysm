# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import *

#### Menu  implementation
def printMenu():
    print("\nWelcome! Crime Manager Program (xml version)")
    print("========Menu==========")
    print("Get crime data from year: g")
    print("Get crime data from age: a")
    print("Get crime data from relation: r")
    print("Get crime data from mental: l")
    print("Get crime data from tool: p")
    print("Get crime data from clue: e")
    print("Quit program:   q")
    print("----------------------------------------")
    print("print Book list: b")
    print("Make html: m")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  'l':
        getCrimeDataFromMENTAL()
    elif menu == 'p':
        getCrimeDataFromTOOL()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'r':
        getCrimeDataFromRELATION()
    elif menu == 'b':
        PrintBookList(["title",])
    elif menu == 'a':
        getCrimeDataFromAGE()
    elif menu == 'e':
        getCrimeDataFromCLUE()
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getCrimeDataFromYEAR(isbn)
        AddBook(ret)
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
