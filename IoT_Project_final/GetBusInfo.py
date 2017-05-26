import json, requests

url = 'http://m.bus.go.kr/mBus/bus/getStationByUid.bms'

params = dict(
    arsId='09107'
)

data = None

def __init__():
    resp = requests.get(url=url, params=params)
    global data
    data = json.loads(resp.text)
    getData()
  #  printData()


def getData():
    busNum = []
    busArrive = []
    for i in data['resultList']:
        # 버스 번호
        a = i['rtNm']
        busNum.append(a)

        # 첫번째 버스 도착 번호
        b = i['arrmsgSec1']
        busArrive.append(b)
    return (busNum, busArrive)


def printData():
    for i in data['resultList'] :
        print(i['rtNm']) #버스번호
        print(i['arrmsgSec1']) #첫번째 버스 도착번호
