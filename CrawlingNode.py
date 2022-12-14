import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QThread
from CrawlingUi import Ui_DomecallCrawling
from ExcelData import getItemList
from bs4 import BeautifulSoup
import time

# 보안할 부분
# 1. Key Value로 데이터 넣기
# 2. 쓰레드 10개로 탐색
# 2.5 쓰레드 올리지말고 크롬드라이버 생성 for문으로 100개 실행하고 i순서대로 값 받으면 됌
# 3 소박스 대박스 try except문으로 있으면 실행 없으면 없음 키 벨류에 넣기
    

class Example(QMainWindow, Ui_DomecallCrawling):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 프로그램이 항상 최상단에 위치하도록 지정(크롬에 가리지 않게)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()


    # start 쓰레드 1(예매페이지 접속)
    class Tread10(QThread):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent

        def run(self):
            for i in range(len(itemList)):
                url = f"https://www.domecall.net/goods/goods_view.php?goodsNo={itemList(i)}"
                request = requests.get(url)
                soup = BeautifulSoup(request.text, 'html.parser')
                price = soup.select_one('#frmView > div > div.item > ul > li.price > div > strong')
                bacode = soup.select_one('#frmView > div > div.item > ul > li:nth-child(2) > div')
                productCode = soup.select_one('#frmView > div > div.item > ul > li:nth-child(3) > div')
                origin = soup.select_one('#frmView > div > div.item > ul > li:nth-child(4) > div')
                bigBoxCount = soup.select_one('#frmView > div > div.item > ul > li:nth-child(5) > div > span')
                smallBoxCount = soup.select_one('#frmView > div > div.item > ul > li:nth-child(6) > div > span')



    # start 쓰레드 1(예매페이지 접속)
    class stop(QThread):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent

        def run(self):
            sys.exit(0)

    # start
    def start(self):
        try:
            global itemList
            global textBrowser
            # Ui 변수 선언
            Ui_startText = self.lineEdit_groupcode.text()
            Ui_endText = self.lineEdit_datecode.text()
            textBrowser = self.textBrowser

            itemList = getItemList(Ui_startText, Ui_endText)

            start_time = time.time()
            Tread10 = Example.Tread10(self)
            Tread10.start()

        except Exception as error:
            print(error)

    def stop(self):
        stop = Example.stop(self)
        stop.start()


app = QApplication([])
ex = Example()
sys.exit(app.exec_())
