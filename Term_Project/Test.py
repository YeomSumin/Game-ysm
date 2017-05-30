import http.client
from xml.dom.minidom import parse, parseString

conn = http.client.HTTPConnection("openapi.crimestats.or.kr:8080")
conn.request("GET", "/WiseOpen/ArcData/BZ9VPQBK6Y4W7CS84PP0/xml/1/400/2015/208/10208/5")
req = conn.getresponse()

ItemNum = 0
DataList = []

def main():
    global ItemNum

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes
            DataList.clear()

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    # if subitems[3].firstChild.nodeValue == InputLabel.get():  # 구 이름이 같을 경우
                    #    pass
                    # elif subitems[5].firstChild.nodeValue == InputLabel.get():    # 동 이름이 같을 경우
                    #    pass

                    if subitems[1].firstChild is not None:
                        DataList.append((subitems[].firstChild.nodeValue, subitems[].firstChild.nodeValue,
                                         subitems[].firstChild.nodeValue))
                    #else:
                        #DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, ""))
                    ItemNum += 1


def sorting(key, r=False):  # 0: 시설명, 1: 주소지, 2: 연락처
    DataList.sort(key=lambda e: e[key], reverse=r)
    print("정렬된 결과 >>>")

    for i in range(len(DataList)):
        print("[{0}] 시설명: {1}, 주소지: {2}, 연락처: {3}".format(i, DataList[i][0], DataList[i][1], DataList[i][2]))

main()