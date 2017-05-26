from tkinter import *
from time import sleep
import GetBusInfo, GetNewsInfo, GetWeatherInfo
import datetime
import webbrowser

newsUrl = None
class MyFrame:
    i = 0
    busInfo = None
    weatherInfo = None
    newsInfo = None

    def __init__(self, parent):

        self.parent = parent
        self.parent.title("Smart Mirror")

        self.myContainer = Frame(parent)
        self.myContainer.pack(fill=BOTH, expand= True)

        self.loadData()
        self.initGUI()

    def dataInit(self):
        global busInfo
        global weatherInfo
        global newsInfo

        busInfo = GetBusInfo.__init__()
        weatherInfo = GetWeatherInfo.__init__()
        newsInfo = GetNewsInfo.__init__()


    def loadData(self):
        self.dataInit()

        # DataSetting
        # TimeInfo
        self.time = datetime.datetime.now().strftime('%Y년 %m월 %d일 %H:%M')
        # WeatherInfo
        self.weather = GetWeatherInfo.getData()
        # NewsInfo
        self.newsInfo = GetNewsInfo.getData()
        # BustInfo
        self.bus = GetBusInfo.getData()


    def initGUI(self):

        self.frameTitle = Frame(self.myContainer, background="black")
        self.frameTitle.pack(fill=X)

        lbltime = Label(self.frameTitle, text=self.time, width=20, foreground='white',
                        background='black', font = "Helvetica 35 bold")
        lbltime.pack(side=TOP, padx=10, pady=10)

        # Title
        self.frameTime = Frame(self.myContainer, background="black")
        self.frameTime.pack(fill=BOTH)

        lblWeatherInfo = Label(self.frameTime, text="<서울시 도봉구 쌍문동 날씨정보>", width=30, foreground='white',
                               background='black', font = "Helvetica 16 bold")
        lblWeatherInfo.pack(side=LEFT, padx=10, pady=10)

        lblTitle = Label(self.frameTime, text="<버스 도착 정보>", width=19, foreground='white', background='black', font = "Helvetica 16 bold")
        lblTitle.pack(side=RIGHT, padx=10, pady=10)

        self.frameStation = Frame(self.myContainer, background="black")
        self.frameStation.pack(fill=BOTH, expand=True)

        # 정류장 이름
        lblStation = Label(self.frameStation, text="덕성여대", width=18, foreground='white', background='black', font = "Helvetica 16 bold")
        lblStation.pack(side=RIGHT, padx=10, pady=8)

        # 온도
        lblTemperature = Label(self.frameStation, text=" 온도 : " + self.weather[0], width=16, foreground='white',
                               background='black', font = "Helvetica 16 bold")
        lblTemperature.pack(side=LEFT, padx=50, pady=2)

        self.frameStationNum = Frame(self.myContainer, background="black")
        self.frameStationNum.pack(fill=X)

        # 정류장 번호
        lblStationNum = Label(self.frameStationNum, text="09-107", width=18, foreground="#ffffff", background="black", font = "Helvetica 16 bold")
        lblStationNum.pack(side=RIGHT, padx=10, pady=8)

        # 날씨
        lblWeather = Label(self.frameStationNum, text=" 날씨 : " + self.weather[1], width=16, foreground="#ffffff",
                           background="black", font = "Helvetica 16 bold")
        lblWeather.pack(side=LEFT, padx=50, pady=2)

        self.frameCityName = Frame(self.myContainer, background="black")
        self.frameCityName.pack(fill=BOTH, expand=True)

        # SEOUL
        lblCityName = Label(self.frameCityName, text="SEOUL", width=18, foreground='white', background='black', font = "Helvetica 16 bold")
        lblCityName.pack(side=RIGHT, padx=10, pady=8)
        
        

        # 강수확률
        lblRainfall = Label(self.frameCityName, text=" 강수확률 : " + self.weather[2], width=16, foreground='white',
                            background='black', font = "Helvetica 16 bold")
        lblRainfall.pack(side=LEFT, padx=50, pady=2)

        # 버스 도착 정보 list
        for i in range(len(self.bus[0])):
            self.frameBus = Frame(self.myContainer, background="black")
            self.frameBus.pack(fill=X)
            plusBusInfo(self.frameBus, self.bus[0][i], self.bus[1][i])


        # 뉴스 Title list
        for i in range(len(self.newsInfo[0])):
            self.frameNews = Frame(self.myContainer, background="black")
            self.frameNews.pack(fill=X)
            plusNewsTitleInfo(self.frameNews, self.newsInfo[0][i], self.newsInfo[1][i])



# 버스 정보
def plusBusInfo(frame, txtBusNum, txtBusArrive):
    # 첫번째 버스 도착 정보
    lblArrmsgSec1 = Label(frame, text=txtBusArrive, width=20, foreground="#ffffff", background='black', font = "Helvetica 16 bold")
    lblArrmsgSec1.pack(side=RIGHT, padx=2, pady=2)

    # 버스 번호
    lblBusNum = Label(frame, text=txtBusNum, width=5, foreground="#ffffff", background='black', font = "Helvetica 16 bold")
    lblBusNum.pack(side=RIGHT, padx=2, pady=2)


# 뉴스 정보
def plusNewsTitleInfo(frame, txtNewsTitle, txtNewsUrl):
    newsUrl = txtNewsUrl
    lblNewsTitle = Label(frame, text=txtNewsTitle, width=40, foreground="#ffffff", background='black', font = "Helvetica 16 bold")
    lblNewsTitle.pack(side=LEFT, padx=5, pady=5)
    lblNewsTitle.bind("<Button-1>",lambda event, text=newsUrl: callback(event,newsUrl))


def callback(event, text):
    webbrowser.open_new(text)
    webbrowser.attributes('-fullscreen', True)

def main():
    root = Tk()
 
    root.geometry("1080x920+900+500")
    root.attributes('-fullscreen', True)
    app = MyFrame(root)
    app.loadData()
    app.initGUI()
   # root.update_idletasks()
    #root.update()
    #sleep(1)
    #app.myContainer.destroy()



 #   while True:
 #       app = MyFrame(root)
  #      app.loadData()
   #     app.initGUI()
    #    root.update_idletasks()
     #   root.update()
     #   sleep(1)
      #  app.myContainer.destroy()

    root.mainloop()

if __name__ == '__main__':
    main()
