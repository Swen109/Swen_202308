import sys
from PyQt5.QtWidgets import *
import pyautogui
import time
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yayi')
        self.initUI()

    def initUI(self):
        SWidth, SHeight = pyautogui.size()
        WWidth, WHeight = SWidth//8, SHeight//4
        x = (SWidth-WWidth)//2
        y = (SHeight-WHeight)//2
        self.setGeometry(x, y, WWidth, WHeight)

        self.vbox = QWidget(self)
        self.vbox.setGeometry(0,WHeight//20,WWidth,WHeight)
        v_layout = QVBoxLayout(self.vbox)

        v_layout.addWidget(QLabel('考試場次數字',self))
        self.opertnTme = QLineEdit()
        v_layout.addWidget(self.opertnTme)
        
        v_layout.addWidget(QLabel('准考證號碼',self))
        self.exmneNo = QLineEdit()
        v_layout.addWidget(self.exmneNo)

        #---以下出生年月日欄位---#
        v_layout.addWidget(QLabel('出生年月日',self))
        h_layout = QHBoxLayout()
        
        self.year = QLineEdit()
        h_layout.addWidget(self.year)

        self.month = QLineEdit()
        h_layout.addWidget(self.month)

        self.day = QLineEdit()
        h_layout.addWidget(self.day)
        #---以上出生年月日欄位---#

        v_layout.addLayout(h_layout)
        v_layout.addStretch(4)

        self.btn1 = QPushButton('取得成績', self)
        v_layout.addWidget(self.btn1)
        v_layout.addStretch(3)

        self.btn1.clicked.connect(self.Btn1Click)

    def Btn1Click(self):
        
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium import webdriver

        self.btn1.setText("等待中")

        driver = webdriver.Chrome()
        driver.get("https://www.topik.go.kr/TWMYPG/TWMYPG0060-001.do")

        def clicktopik(xpath):
            # c1 = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            c1= driver.find_element(By.XPATH,xpath)
            c1.click()


        Q1 = driver.find_elements(By.XPATH, '//*[@id="closePoint"]') #找跳出視窗

        if bool(Q1) == True :
            clicktopik('//*[@id="closePoint"]') #如果有找到就關閉一開始的視窗
            clicktopik('//a[@class="btns btns_m btns_ok"][@title="성적확인"]') #點進輸入頁面
        else:
            clicktopik('//a[@class="btns btns_m btns_ok"][@title="성적확인"]') #點進輸入頁面

        print(str(self.year.text))

        #點進輸入頁面 場次 輸入准考證 出生年月日
        clicktopik(f'//option[@value="T00{self.opertnTme.text()}"]')
        exmeNO = driver.find_element(By.XPATH,'//*[@id="exmneNo"]')
        exmeNO.clear()
        exmeNO.send_keys(self.exmneNo.text())
        clicktopik(f'//option[@value="{self.year.text()}"]')
        clicktopik(f'//option[@value="{self.month.text()}"]')
        clicktopik(f'//option[@value="{self.day.text()}"]')
        clicktopik('//a[@title="검색"][@href="javascript:fnSearch()"]')
        time.sleep(10)
        clicktopik('//a[@title="출력"]')

        while True:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
    