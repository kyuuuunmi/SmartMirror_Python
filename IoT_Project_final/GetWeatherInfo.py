import xmltodict, json, requests

urlwheather = 'http://www.kma.go.kr/wid/queryDFS.jsp'

paramswheather = dict(
    ##서울시 도봉구 쌍문동의 xy좌표
    gridx='61',
    gridy='128'
)

data = None

def __init__():
    global data
    resp = requests.get(url=urlwheather, params=paramswheather)
    data = xmltodict.parse(resp.text)
    json.dumps(data)
    getData()
    #printData()


def getData():
    temperature = data['wid']['body']['data'][0]['temp']
    weather = data['wid']['body']['data'][0]['wfKor']
    rainfall = data['wid']['body']['data'][0]['pop']
    return (temperature, weather, rainfall)


def printData():
    print(data['wid']['body']['data'][0]['temp'])  # 현재온도
    print(data['wid']['body']['data'][0]['wfKor'])  # 날씨 한마디
    print(data['wid']['body']['data'][0]['pop'])  # 강수확률

