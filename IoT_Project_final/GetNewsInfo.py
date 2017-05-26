import xmltodict, json, requests

urlnews = 'http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=morning_news'

datanews = None

def __init__():
    global datanews
    resnews = requests.get(url=urlnews)
    datanews = xmltodict.parse(resnews.text)
    json.dumps(datanews)

    getData()
    #printData()



def getData():
    newsTitle = []
    newsUrl = []
    for i in  datanews['rss']['channel']['item'] :
        # newTitle
        a = i['title']
        newsTitle.append(a)

        # newUrl
        b = i['link']
        newsUrl.append(b)
    return (newsTitle, newsUrl)


def printData():
    #기사 title
    for i in datanews['rss']['channel']['item'] :
        print(i['title'])

